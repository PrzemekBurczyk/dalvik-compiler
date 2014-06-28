'''
Created on 3 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from items.proto_id_item import ProtoIdItem


class ProtoIdItemSection(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        proto_id_item = ProtoIdItem(self)
        proto_id_item.shorty_idx = 4
        proto_id_item.return_type_idx = 2
        proto_id_item.parameters_off.ref = 0
        self.data.append(proto_id_item)
        
        proto_id_item = ProtoIdItem(self)
        proto_id_item.shorty_idx = 5
        proto_id_item.return_type_idx = 2
        proto_id_item.parameters_off.ref = self.getRoot().type_list_section.data[0]
        self.data.append(proto_id_item)
        