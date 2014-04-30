from pynag.Model.nagios_objects import *

class ShinkenHost(Host):
    object_type = 'host'
    objects = ObjectFetcher('host')
