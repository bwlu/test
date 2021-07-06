# -*- coding: utf-8 -*-
# @Date    : 2019-08-28 11:04:05
# @Author  : bwlu
# @Version : 

from django.db import connections

__all__ = ['close_old_connections']

def close_old_connections():
    for conn in connections.all():
        conn.close_if_unusable_or_obsolete()