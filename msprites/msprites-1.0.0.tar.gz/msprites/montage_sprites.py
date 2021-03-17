import os
import shutil
import tempfile
from msprites.command import Command
from msprites import FFmpegThumbnails
from msprites.settings import Settings
from msprites.constants import THUMBNAIL_SPRITESHEET
from msprites.webvtt import WebVTT
from msprites.temp_file import TempFile


class MontageSprites(Settings):

    def __init__(self, thumbs):
        self.thumbs: FFmpegThumbnails = thumbs
        self.dir = tempfile.TemporaryDirectory()

    def dest(self):
        return os.path.join(self.dir.name, self.FILENAME_FORMAT.format(ext=self.EXT))

    def generate(self):
        cmd  = THUMBNAIL_SPRITESHEET.format(
            rows=self.ROWS,
            cols=self.COLS,
            width=self.WIDTH,
            height=self.HEIGHT,
            input=self.thumbs.dir.name,
            output=self.dest()
        )
        Command.execute(cmd)

    def cleanup(self):
        try:
            self.dir.cleanup()
            self.thumbs.cleanup()
        except Exception:
            pass

    def count(self):
        splist = os.listdir(self.dir.name)
        return len(splist)

    def to_webvtt(self, create_webvtt):
        if not create_webvtt:
            return
        webvtt = WebVTT(self)
        webvtt.generate()

    def copy_to(self, to):
        os.makedirs(to, exist_ok=True)
        shutil.copytree(self.dir.name, to)


    @classmethod
    def from_media(cls, path, create_webvtt=True, to_dest=None):
        sprites = MontageSprites(FFmpegThumbnails.from_media(path))
        sprites.generate()
        sprites.to_webvtt(create_webvtt)
        if to_dest:
            sprites.copy(to_dest)
            sprites.cleanup()
        return sprites
