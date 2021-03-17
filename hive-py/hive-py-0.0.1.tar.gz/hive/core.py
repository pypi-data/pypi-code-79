import json
import time

class HivePubSub:
    def subscribe_raw(self, topic, callback):
        """
        Subscribe to the bytes received on a topic

        :param topic: topic name
        :param callback: callback function to execute - cb(bytes)
        :return: None
        """
        pass

    def publish_raw(self, topic, message):
        """
        Publish raw bytes to a topic
        :param topic: topic to subscribe
        :param message: message bytes to publish
        :return:
        """
        pass

    def spin(self):
        '''
        Start the broker connection and take over the main thread
        :return:
        '''
        while True:
            time.sleep(0.01)


class Publisher:

    def __init__(
            self,
            pubsub,
            topic,
            cls,
            encoder
    ):
        self.pubsub = pubsub
        self.topic = topic
        self.cls = cls
        self.encoder = encoder

    def publish(self, obj):
        self.pubsub.publish_raw(self.topic, self.encoder(self.cls, obj))


class Subscriber:

    def __init__(
            self,
            pubsub,
            topic,
            cls,
            decoder,
            callback
    ):
        pubsub.subscribe_raw(
            topic,
            Subscriber.raw_handler(cls, decoder, callback)
        )

    @staticmethod
    def raw_handler(cls, decoder, callback):
        def handler(b):
            callback(decoder(cls, b))
        return handler


class JsonEncoder:
    def __call__(self, _, obj):
        return json.dumps(obj.__dict__).encode("utf-8")


class JsonDecoder:

    @staticmethod
    def dict_to_obj(cls):
        def builder(d):
            obj = cls()
            for key, value in d.items():
                setattr(obj, key, value)
            return obj

        return builder

    def __call__(self, cls, bytes):
        return json.loads(bytes.decode("utf-8"), object_hook=JsonDecoder.dict_to_obj(cls))


class Hive:
    DEFAULT_PUBSUB = HivePubSub
    DEFAULT_ENCODER = JsonEncoder
    DEFAULT_DECODER = JsonDecoder

    def __init__(self, pubsub=None, encoder=None, decoder=None,):
        self.pubsub = (pubsub or Hive.DEFAULT_PUBSUB())
        self.encoder = (encoder or Hive.DEFAULT_ENCODER())
        self.decoder = (decoder or Hive.DEFAULT_DECODER())

    def spin(self):
        self.pubsub.spin()

    def publisher(self, topic, cls):
        return Publisher(self.pubsub, topic, cls, self.encoder)

    def subscribe(self, topic, cls, callback):
        return Subscriber(self.pubsub, topic, cls, self.decoder, callback)
