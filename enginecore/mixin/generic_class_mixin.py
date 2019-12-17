"""
    Created by Sayem on 20 January, 2019
"""
import re

from django.db.models import ManyToManyField

__author__ = "sayem"


class Model2DictMixin(object):
    def to_dict(self):
        if not self.pk:
            return []
        _fields = self._meta.concrete_fields + self._meta.many_to_many
        _data = {}
        for _field in _fields:
            if "_ptr" in _field.name:
                continue
            elif isinstance(_field, ManyToManyField):
                _data[_field.name] = list(_field.value_from_object(obj=self).values_list("id", flat=True))
            _data[_field.name] = _field.value_from_object(obj=self)
        return _data


class CodedModelMixin(object):
    @classmethod
    def prefix(cls):
        return re.sub(r'[a-z\d]+|(?<=[A-Z])[A-Z\d]+', r'', cls.__name__)

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @property
    def max_sequence_context_name(self):
        return self.__class__.__name__

    @property
    def code_prefix(self):
        return self.__class__.prefix()

    @property
    def code_separator(self):
        return "-"
