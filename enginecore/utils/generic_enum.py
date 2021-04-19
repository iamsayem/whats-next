"""
    Created by Sayem on 29 November, 2019
"""
from enum import Enum

__author__ = "sayem"


class GenericEnum(Enum):
    @classmethod
    def get_choice_name(cls, value):
        for _tag in cls:
            if _tag.value == value:
                return _tag.name
        return None

    @classmethod
    def get_choice_value(cls, name):
        for _tag in cls:
            if _tag.name == name:
                return _tag.value
        return None

    @classmethod
    def get_choices(cls):
        return [(_tag.name, _tag.value) for _tag in cls]
