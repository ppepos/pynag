import nagios_objects
from all_attributes import AllAttributes

class StringToClass(object):

    def __init__(self, backend='nagios'):
        
        self.backend = backend

        if backend == 'nagios':
            # Default Nagios objects
            # No prefix for backwards compatibility
            self.string_to_class = {}
            self.string_to_class['contact'] = nagios_objects.Contact
            self.string_to_class['service'] = nagios_objects.Service
            self.string_to_class['host'] = nagios_objects.Host
            self.string_to_class['hostgroup'] = nagios_objects.Hostgroup
            self.string_to_class['contactgroup'] = nagios_objects.Contactgroup
            self.string_to_class['servicegroup'] = nagios_objects.Servicegroup
            self.string_to_class['timeperiod'] = nagios_objects.Timeperiod
            self.string_to_class['hostdependency'] = nagios_objects.HostDependency
            self.string_to_class['servicedependency'] = nagios_objects.ServiceDependency
            self.string_to_class['hostescalation'] = nagios_objects.HostEscalation
            self.string_to_class['serviceescalation'] = nagios_objects.ServiceEscalation
            self.string_to_class['command'] = nagios_objects.Command

            self.default = nagios_objects.ObjectDefinition
            self.all_attributes = AllAttributes(backend=self.backend)

            nagios_objects.register_properties(self.string_to_class, 
                                                self.all_attributes)

    # for dictionary-like access ['host']
    def __getitem__(self, item, default=None):
        if default != None:
            ret_value = self.string_to_class.get(item, default)
        else:
            ret_value = self.string_to_class.get(item, self.default)
        return ret_value

    def get(self, classname, default=None):
        return self.__getitem__(classname, default)

