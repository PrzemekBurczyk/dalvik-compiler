'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.type_list import TypeList


class TypeListSection(Measurable):
    '''
    classdocs
    '''

    def append(self, type_list):
        if len(self.data) > 0:
            last_type_list = self.data[-1]
            last_type_list.data.append(last_type_list.zeros)
        self.data.append(type_list)

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        # it holds Bytes(self, 2) between it's items! no zero bytes at the end!
        
        type_list = TypeList(self)
        type_list.size.value = 1
        # type_list.typeIdItem.value = 3
        type_list.typeIdItem.ref_type = "index"
        type_list.typeIdItem.ref = self.getRoot().type_id_item_section.data[3]
        self.append(type_list)