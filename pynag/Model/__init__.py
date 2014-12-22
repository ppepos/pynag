# -*- coding: utf-8 -*-
#
# pynag - Python Nagios plug-in and configuration environment
# Copyright (C) 2011 Pall Sigurdsson
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


"""
This module provides a high level Object-Oriented wrapper
around pynag.Parsers.config.

Example:

>>> from pynag.Model import Service, Host
>>>
>>> all_services = Service.objects.all
>>> my_service = all_services[0]
>>> print my_service.host_name # doctest: +SKIP
localhost
>>>
>>> example_host = Host.objects.filter(host_name="host.example.com")
>>> canadian_hosts = Host.objects.filter(host_name__endswith=".ca")
>>>
>>> for i in canadian_hosts:
...     i.alias = "this host is located in Canada"
...     i.save() # doctest: +SKIP
"""

import pynag.errors
import pynag.Utils

from pynag import Parsers
from nagios_objects import *

# Default value returned when a macro cannot be found
_UNRESOLVED_MACRO = ''

# We know that a macro is a custom variable macro if the name
# of the macro starts with this prefix:
_CUSTOM_VARIABLE_PREFIX = '_'

__all__ = [
        'nagios_objects',
        'attribute_list',
        ]


class ModelError(pynag.errors.PynagError):
    """Base class for errors in this module."""


class InvalidMacro(ModelError):
    """Raised when a method is inputted with an invalid macro."""


if __name__ == '__main__':
    pass

