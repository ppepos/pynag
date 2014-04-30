from nagios_objects import *
from shinken_objects import *
class StringToClass(object):

    def __init__(self, backend='nagios'):
        self.backend = backend

        self.string_to_class = {}
        self.string_to_class['contact'] = Contact
        self.string_to_class['service'] = Service
        self.string_to_class['host'] = Host
        self.string_to_class['hostgroup'] = Hostgroup
        self.string_to_class['contactgroup'] = Contactgroup
        self.string_to_class['servicegroup'] = Servicegroup
        self.string_to_class['timeperiod'] = Timeperiod
        self.string_to_class['hostdependency'] = HostDependency
        self.string_to_class['servicedependency'] = ServiceDependency
        self.string_to_class['hostescalation'] = HostEscalation
        self.string_to_class['serviceescalation'] = ServiceEscalation
        self.string_to_class['command'] = Command

        self.shinken_string_to_class = {}
        self.shinken_string_to_class['contact'] = Contact
        self.shinken_string_to_class['service'] = Service
        self.shinken_string_to_class['host'] = ShinkenHost
        self.shinken_string_to_class['hostgroup'] = Hostgroup
        self.shinken_string_to_class['contactgroup'] = Contactgroup
        self.shinken_string_to_class['servicegroup'] = Servicegroup
        self.shinken_string_to_class['timeperiod'] = Timeperiod
        self.shinken_string_to_class['hostdependency'] = HostDependency
        self.shinken_string_to_class['servicedependency'] = ServiceDependency
        self.shinken_string_to_class['hostescalation'] = HostEscalation
        self.shinken_string_to_class['serviceescalation'] = ServiceEscalation
        self.shinken_string_to_class['command'] = Command

    def get(self, classname, default=ObjectDefinition, backend='nagios'):
        try:
            if self.backend == 'nagios':
                a = self.getNagiosClass(classname, default)
            elif self.backend == 'shinken':
                a = self.getShinkenClass(classname, default)
        except:
            return default
        return a

    def getNagiosClass(self, classname, default):
        return self.string_to_class.get(classname, default)

    def getShinkenClass(self, classname, default):
        return self.shinken_string_to_class.get(classname, default)
