"""
    Created by Sayem on 12 October, 2019
"""
__author__ = "sayem"

from .apps import INSTALLED_APPS as PROJECT_APPS
from .database import *
from .celery_config import *

__all__ = [
    "PROJECT_APPS",
    "DATABASES",
    "BROKER_URL",
    "CELERY_TIMEZONE"
]
