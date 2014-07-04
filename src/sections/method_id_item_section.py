'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.method_id_item import MethodIdItem


class MethodIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        method_id_item = MethodIdItem(self)
        # method_id_item.classIdx.value = 0
        method_id_item.classIdx.ref_type = "index"
        method_id_item.classIdx.ref = self.getRoot().type_id_item_section.data[0]
        # method_id_item.protoIdx.value = 0
        method_id_item.protoIdx.ref_type = "index"
        method_id_item.protoIdx.ref = self.getRoot().proto_id_item_section.data[0]
        # method_id_item.nameIdx.value = 0
        method_id_item.nameIdx.ref_type = "index"
        method_id_item.nameIdx.ref = self.getRoot().string_id_item_section.data[0]
        self.data.append(method_id_item)
        
        method_id_item = MethodIdItem(self)
        # method_id_item.classIdx.value = 0
        method_id_item.classIdx.ref_type = "index"
        method_id_item.classIdx.ref = self.getRoot().type_id_item_section.data[0]
        # method_id_item.protoIdx.value = 1
        method_id_item.protoIdx.ref_type = "index"
        method_id_item.protoIdx.ref = self.getRoot().proto_id_item_section.data[1]
        # method_id_item.nameIdx.value = 7
        method_id_item.nameIdx.ref_type = "index"
        method_id_item.nameIdx.ref = self.getRoot().string_id_item_section.data[7]
        self.data.append(method_id_item)
        
        method_id_item = MethodIdItem(self)
        # method_id_item.classIdx.value = 1
        method_id_item.classIdx.ref_type = "index"
        method_id_item.classIdx.ref = self.getRoot().type_id_item_section.data[1]
        # method_id_item.protoIdx.value = 0
        method_id_item.protoIdx.ref_type = "index"
        method_id_item.protoIdx.ref = self.getRoot().proto_id_item_section.data[0]
        # method_id_item.nameIdx.value = 0
        method_id_item.nameIdx.ref_type = "index"
        method_id_item.nameIdx.ref = self.getRoot().string_id_item_section.data[0]
        self.data.append(method_id_item)