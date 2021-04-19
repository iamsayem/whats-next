"""
    Created by Sayem on 29 November, 2019
"""
from datetime import datetime

__author__ = "sayem"


class Clock(object):
    @staticmethod
    def timestamp(_format='ms'):
        if _format == 'ms':
            return round(datetime.now().timestamp() * 1000)
        return round(datetime.now().timestamp())

    @staticmethod
    def convert_str_to_date_obj(date_str="", fmt="%d-%m-%Y"):
        _datetime_obj = datetime.strptime(date_str, fmt)
        return _datetime_obj.date()
