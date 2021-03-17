# +
import os
import math
import time

import numpy
import cv2
import pytesseract
import mss
import regex
import pynput

import craft_text_detector as craft

from torch import cuda
from IPython.display import display, HTML, Image

LOG_NONE, LOG_INFO, LOG_ALL = 0, 1, 2

def scale_number(from_val, from_min, from_max, to_min, to_max):
    return round((to_max - to_min) * (from_val - from_min) / (from_max - from_min) + to_min)


def _button(name):
    return {
        "left": pynput.mouse.Button.left, 
        "right": pynput.mouse.Button.right, 
        "middle": pynput.mouse.Button.middle
    }[name.lower()]


def notebook_image(temp, file, comment=None):
    with open(os.path.join(temp, file), 'rb') as f:
        image = f.read()

    display(create_gallery([(image, comment if comment else file)]))


def notebook_image_marked(image, *marks, comment=""):
    image = image.copy()
    for center in marks:
        image = cv2.circle(image, center, 20, (0, 0, 255), 3)
    is_success, im_buf_arr = cv2.imencode(".png", image)
    byte_im = im_buf_arr.tobytes()

    display(create_gallery([(byte_im, comment)]))


def _src_from_data(data):
    """Base64 encodes image bytes for inclusion in an HTML img element"""
    img_obj = Image(data=data)
    for bundle in img_obj._repr_mimebundle_():
        for mimetype, b64value in bundle.items():
            if mimetype.startswith('image/'):
                return f'data:{mimetype};base64,{b64value}'


def create_gallery(images, row_height='auto'):
    figures = []
    for image, caption in images:
        src = _src_from_data(image)

        figures.append(f'''
            <figure style="margin: 5px !important;">
              <img src="{src}" style="height: {row_height}">
              {caption}
            </figure>
        ''')
    return HTML(data=f'''
        <div style="display: flex; flex-flow: row wrap; text-align: center;">
        {''.join(figures)}
        </div>
    ''')


# -
class OpenRPA:
    def __init__(self):
        self.freezed = False
        self.log_level = LOG_NONE
        self.monitor = None

        self.bgr = None
        self.rgb = None
        self.grey = None

        self.text_areas = None
        self.text_lines = None
        self.text_words = None

        self.image_path = 'screen_shot.png'
        self.temp_dir = "temp/"
        self.num_searches = 0

        self.refine_net = None
        self.craft_net = None

        self.cuda = cuda.is_available()
        self.mouse = pynput.mouse.Controller()

    def scale_xy(self, x, y):
        return (
            scale_number(x, 0, self.rgb.shape[1], self.monitor["left"], self.monitor["left"] + self.monitor["width"]), 
            scale_number(y, 0, self.rgb.shape[0], self.monitor["top"], self.monitor["top"] + self.monitor["height"]))
        
    def set_log_level(self, level):
        if level == "NONE":
            level = LOG_NONE
        elif level == "INFO":
            level = LOG_INFO
        elif level == "ALL":
            level = LOG_ALL
        self.log_level = level
        
    def freeze(self):
        if not self.freezed:
            self.screenshot()
            self.detect_text()
            self.recognize_text()
            self.freezed = True

    def screenshot(self, monitor=1):
        with mss.mss() as sct:
            self.monitor = sct.monitors[monitor]
            bgra = numpy.array(sct.grab(self.monitor))

        self.bgr = cv2.cvtColor(bgra, cv2.COLOR_BGRA2BGR)
        self.rgb = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2RGB)

        if self.log_level >= LOG_ALL:
            f = os.path.join(self.temp_dir, self.image_path)
            cv2.imwrite(f, self.bgr)
            notebook_image(self.temp_dir, self.image_path)

    def detect_text(self):
        if not self.refine_net:
            self.refine_net = craft.load_refinenet_model(cuda=self.cuda)
            self.craft_net = craft.load_craftnet_model(cuda=self.cuda)

        # perform prediction
        self.text_areas = craft.get_prediction(
            image=self.rgb,
            craft_net=self.craft_net,
            refine_net=self.refine_net,
            text_threshold=0.7,
            link_threshold=0.4,
            low_text=0.4,
            cuda=self.cuda,
            long_size=1280
        )

        if self.log_level >= LOG_INFO:
            # export heatmap, detection points, box visualization
            craft.export_extra_results(
                image_path=self.image_path,
                image=self.rgb,
                regions=self.text_areas["boxes"],
                heatmaps=self.text_areas["heatmaps"],
                output_dir=self.temp_dir
            )

            file = os.path.splitext(self.image_path)[0]
            notebook_image(self.temp_dir, "%s_text_detection.png" % file)
            
            if self.log_level >= LOG_ALL:
                notebook_image(self.temp_dir, "%s_text_score_heatmap.png" % file)
                notebook_image(self.temp_dir, "%s_link_score_heatmap.png" % file)

    def recognize_text(self):
        self.text_words, self.text_lines, images = [], [], []

        for (left, top), (right, _), (_, bottom), (_, _) in self.text_areas['boxes']:

            region = self.bgr[round(top):round(bottom), round(left):round(right)]
            d = pytesseract.image_to_data(region, output_type=pytesseract.Output.DICT)

            words_in_line = []
            for text, conf, x, y, w, h in zip(d['text'], map(float, d['conf']), d['left'], d['top'], d['width'], d['height']):
                if conf > 0 and text:
                    words_in_line.append({
                        "left": round(left + x),
                        "top": round(top + y),
                        "width": round(w),
                        "height": round(h),
                        "text": text.strip(),
                        "conf": conf,
                        "center": (round(left + x + w / 2), round(top + y + h / 2))
                    })

            if words_in_line:
                self.text_words += words_in_line

                line = {
                    "left": round(left),
                    "top": round(top),
                    "width": round(right - left),
                    "height": round(bottom - top),
                    "text": " ".join([word["text"] for word in words_in_line]),
                    "conf": sum([word["conf"] for word in words_in_line]) // len(words_in_line),
                    "center": (round((left + right) / 2), round((top + bottom) / 2)),
                }
                self.text_lines.append(line)

                if self.log_level >= LOG_ALL:
                    is_success, im_buf_arr = cv2.imencode(".png", region)
                    byte_im = im_buf_arr.tobytes()
                    images.append((byte_im, line["text"]))

        if self.log_level >= LOG_ALL:
            display(create_gallery(images))

    def _store_search_image(self, image, comment=None):
        filename = f"{self.num_searches:03}_search.png"
        self.num_searches += 1
        f = os.path.join(self.temp_dir, filename)
        cv2.imwrite(f, image)
        notebook_image(self.temp_dir, filename, comment=comment)

    def search_line(self, pattern, distance=0):
        self.freeze()
        return self._search_text(self.text_lines, pattern, distance)

    def search_word(self, pattern, distance=0):
        self.freeze()
        return self._search_text(self.text_words, pattern, distance)

    def _search_text(self, text, pattern, distance):
        pattern = r'(?e)(%s){e<=%d}' % (pattern, distance)
        matches = [match for match in text if regex.search(pattern, match["text"], flags=regex.IGNORECASE)]

        if self.log_level >= LOG_INFO:
            image = self.bgr.copy()
            for d in matches:
                image = cv2.rectangle(image, (d["left"], d["top"]),
                                      (d["left"] + d["width"], d["top"] + d["height"]), (0, 0, 255), 3)
                image = cv2.circle(image, d["center"], 20, (0, 0, 255), 3)
            self._store_search_image(image, pattern)

        return matches

    def search_image(self, filename, threshold=0.8, best_match=False):
        self.freeze()

        if self.grey is None:
            self.gray = cv2.cvtColor(self.bgr, cv2.COLOR_BGR2GRAY)

        template = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]

        res = cv2.matchTemplate(self.gray, template, cv2.TM_CCOEFF_NORMED)

        matches = []
        if best_match:
            _, val, _, loc = cv2.minMaxLoc(res)
            if val >= threshold:
                matches.append({
                    "left": loc[0], "right": loc[0] + w,
                    "top": loc[1], "bottom": loc[1] + h,
                    "center": (loc[0] + w // 2, loc[1] + h // 2)
                })
        else:
            loc = numpy.where(res >= threshold)

            for pt in zip(*loc[::-1]):
                cx, cy = pt[0] + w // 2, pt[1] + h // 2
                if not any([d["left"] < cx < d["right"] and d["top"] < cy < d["bottom"] for d in matches]):
                    matches.append({
                        "left": pt[0], "right": pt[0] + w,
                        "top": pt[1], "bottom": pt[1] + h,
                        "center": (cx, cy)
                    })

        if self.log_level >= LOG_INFO:
            bgr = self.bgr.copy()
            for d in matches:
                cv2.rectangle(bgr, (d["left"], d["top"]), (d["right"], d["bottom"]), (0,0,255), 3)

            self._store_search_image(bgr, filename)

        return matches

    def mouse_position(self, x, y):
        self.mouse.position = self.scale_xy(x, y)

    def mouse_press(self, button="left"):
        self.mouse.press(_button(button))

    def mouse_release(self, button="left"):
        self.mouse.release(_button(button))

    def mouse_click(self, button="left", count="1"):
        self.mouse.click(_button(button), int(count))

    def mouse_scroll(self, dx, dy):
        self.mouse.scroll(dx, dy)

    def mouse_click_position(self, x, y, button="left", count="1"):
        self.mouse_position(x, y)
        self.mouse_click(button, count)

    def click_word(self, text):
        self.freeze()
        result = self.search_word(text)
        if result:
            self.mouse_click_position(*result[0]["center"])
        elif self.log_level >= LOG_ALL:
            notebook.notebook_print("%s no match")

    def click_image(self, filename):
        self.freeze()
        result = self.search(filename, 0.8, True)
        if result:
            self.click(*result[0]["center"])
        elif self.log_level >= LOG_ALL:
            notebook.notebook_print("%s no match")

    def unload_models(self):
        if self.refine_net:
            # unload models from gpu
            craft.empty_cuda_cache()
            self.refine_net = None
            self.craft_net = None



openrpa = OpenRPA()
openrpa.set_log_level("INFO")
openrpa.freeze()

openrpa.click_word("File")


