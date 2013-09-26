#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2013 laoxu

class ObjectDict(dict):
    """ from tornado.util import ObjectDict
    Makes a dictionary behave like an object, with attribute-style access.
    """
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        self[name] = value