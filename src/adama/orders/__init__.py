# -*- coding: utf-8

import os
import sys

from ..commandment import OrderError


def get_template(name):
    """
    """
    template_path = os.path.join(
        os.path.dirname(__path__[0]), 'templates', '{0}.template'.format(name)
    )
    with open(template_path) as template:
        return template.read()


def get_module(module_name, path):
    """Adds a path to a pythonpath and imports and returns a module
    """
    if path and path not in sys.path:
        sys.path.append(path)
    try:
        module = __import__(module_name)
    except ImportError as e:
        raise OrderError(str(e))
    return module


def touch(filename, times=None):
    """Creates an empty file
    """
    with file(filename, 'a'):
        os.utime(filename, times)

