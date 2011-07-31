# -*- coding: utf-8 -*-

"""
"""

import sys
import os

from .commandment import Commander, OrderError


def sir_yes_sir(module='', argv=None):
    """
    """
    argv = argv if argv else sys.argv[:]
    command = os.path.basename(argv[0])
    module = module if module else command
    commander = Commander(command, module)

    no_arg = len(argv) == 1
    needs_help = not no_arg and argv[1] == 'help'
    global_help = needs_help and len(argv) == 2
    order_help = needs_help and len(argv) > 2

    if no_arg or global_help:
        commander.explanations()
        return 0
    else:
        order_name = argv[1] if not order_help else argv[2]
        try:
            order = commander[order_name]
        except KeyError as e:
            return commander(argv[1:])
        else:
            if order_help:
                order.explanations()
                return 0
            else:
                return order(argv[1:])
