# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import attr
import feedgenerator


@attr.s
class Entry(object):
    title = attr.ib()
    content = attr.ib()
    link = attr.ib()
    description = attr.ib()
    author = attr.ib()
    updated = attr.ib()
    published = attr.ib()

