'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable
from src.items.type_list import TypeList


class TypeListSection(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def append(self, type_list):
        if len(self.data) > 0:
            last_type_list = self.data[-1]
            if last_type_list.size._value % 2 != 0:
                last_type_list.data.append(last_type_list.zeros)
        self.data.append(type_list)

    def add(self, size, *type_id_idxs):
        type_list = TypeList(self)
        type_list.size.value = size
        for type_id_idx in type_id_idxs:
            bytes = Bytes(type_list, 2)
            bytes.ref_type = "index"
            bytes.ref = type_id_idx
            type_list.data.append(bytes)

        for item in self.data:
            item_size = item.size
            the_same = True
            if item_size != size:
                continue
            for i in range(1, item_size + 1):
                current_type_id_idx = type_list.data[i].ref.parent.getItemIndex(type_list.data[i].ref)
                existing_type_id_idx = item.data[i].ref.parent.getItemIndex(item.data[i].ref)
                if current_type_id_idx != existing_type_id_idx:
                    the_same = False
                    break
            if the_same:
                return item

        self.append(type_list)
        return type_list

    def initialize(self):
        self.add(1, self.getRoot().type_id_item_section.data[3])