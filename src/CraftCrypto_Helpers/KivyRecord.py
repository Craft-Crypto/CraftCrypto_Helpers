from kivy.event import EventDispatcher
from .BaseRecord import BaseRecord


class KivyRecord(EventDispatcher):
    def __init__(self, **kwargs):
        self.keys = BaseRecord().to_dict()
        for key in self.keys:
            self.create_property(key, value=self.keys[key])
        super(KivyRecord, self).__init__(**kwargs)

    def set_record(self, rec, *args):
        for key in rec:
            if args:
                setattr(self, key, rec[key])
            elif not key == 'active':
                setattr(self, key, rec[key])

    def get_record(self):
        new_rec = {}
        for key in self.keys:
            if not getattr(self, key) == '':
                new_rec[key] = getattr(self, key)
        return new_rec

    def get_all(self):
        new_rec = {}
        for key in self.keys:
            new_rec[key] = getattr(self, key)
        return new_rec

    def reset(self, *args):
        my_id = self.my_id
        self.set_record(BaseRecord().to_dict())
        self.my_id = my_id

