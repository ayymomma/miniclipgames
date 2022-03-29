

class VoiceManager(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(VoiceManager, cls).__new__(cls)
        return cls.instance