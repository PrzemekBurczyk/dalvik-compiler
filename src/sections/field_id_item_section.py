'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.field_id_item import FieldIdItem
from src.parser.measurable import Measurable


class FieldIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def add(self, class_idx, return_type_idx, name_idx):
        field_id_item = FieldIdItem(self)
        field_id_item.classIdx.ref_type = "index"
        field_id_item.classIdx.ref = class_idx
        field_id_item.returnTypeIdx.ref_type = "index"
        field_id_item.returnTypeIdx.ref = return_type_idx
        field_id_item.nameIdx.ref_type = "index"
        field_id_item.nameIdx.ref = name_idx

        currentClassIdx = class_idx.parent.getItemIndex(class_idx)
        currentReturnTypeIdx = return_type_idx.parent.getItemIndex(return_type_idx)
        currentNameIdx = name_idx.parent.getItemIndex(name_idx)

        for item in self.data:
            existingClassIdx = item.classIdx.ref.parent.getItemIndex(item.classIdx.ref)
            existingReturnTypeIdx = item.returnTypeIdx.ref.parent.getItemIndex(item.returnTypeIdx.ref)
            existingNameIdx = item.nameIdx.ref.parent.getItemIndex(item.nameIdx.ref)

            if currentClassIdx == existingClassIdx and currentReturnTypeIdx == existingReturnTypeIdx and currentNameIdx == existingNameIdx:
                return item

        self.data.append(field_id_item)
        self.data.sort(cmp=None, key=lambda x: (x.classIdx.ref.parent.getItemIndex(x.classIdx.ref),
                                                x.nameIdx.ref.parent.getItemIndex(x.nameIdx.ref),
                                                x.returnTypeIdx.ref.parent.getItemIndex(x.returnTypeIdx.ref)), reverse=False)
        return field_id_item

    def initialize(self):
        pass