# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseConf(object):
    def get(self):
        pass


class LocalConf(BaseConf):
    pass


class S3Conf(BaseConf):
    def __init__(self):
