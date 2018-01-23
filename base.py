

class BaseMessaging(object):
    def __init__(self, *kargs):
        self.config = kargs.copy()

    def post_message(self, **kargs):
        raise Exception("Not implemented")

    @classmethod
    def parse_toml(cls, toml_dict):
        raise Exception("Not implemented")
