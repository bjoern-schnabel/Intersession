from items import *
from weapons import *
from shields import *
from potions import *
from statuses import *
from custom import *

def get_classes_dict():
    classes_dict = {}
    for cls in globals().values():
        if isinstance(cls, type) and hasattr(cls, 'name'):
            classes_dict[cls.name.lower()] = cls
    return classes_dict

if __name__ == "__main__":
    for i in get_classes_dict():
        print(i)
