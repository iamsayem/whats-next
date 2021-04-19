"""
    Created by Sayem on 29 November, 2019
"""
from django.db.models import Manager

__author__ = "sayem"


class RootEntityModelManager(Manager):
    def get_queryset(self):
        _queryset = super(RootEntityModelManager, self).get_queryset()
        return _queryset.filter(is_active=True, is_deleted=False)
