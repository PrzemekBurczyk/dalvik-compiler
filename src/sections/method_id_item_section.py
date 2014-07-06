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

    def add(self, class_idx, proto_idx, name_idx):
        method_id_item = MethodIdItem(self)
        method_id_item.classIdx.ref_type = "index"
        method_id_item.classIdx.ref = class_idx
        method_id_item.protoIdx.ref_type = "index"
        method_id_item.protoIdx.ref = proto_idx
        method_id_item.nameIdx.ref_type = "index"
        method_id_item.nameIdx.ref = name_idx

        currentClassIdx = class_idx.parent.getItemIndex(class_idx)
        currentProtoIdx = proto_idx.parent.getItemIndex(proto_idx)
        currentNameIdx = name_idx.parent.getItemIndex(name_idx)

        for item in self.data:
            existingClassIdx = item.classIdx.ref.parent.getItemIndex(item.classIdx.ref)
            existingProtoIdx = item.protoIdx.ref.parent.getItemIndex(item.protoIdx.ref)
            existingNameIdx = item.nameIdx.ref.parent.getItemIndex(item.nameIdx.ref)

            if currentClassIdx == existingClassIdx and currentProtoIdx == existingProtoIdx and currentNameIdx == existingNameIdx:
                return item

        self.data.append(method_id_item)
        self.data.sort(cmp=None, key=lambda x: (x.classIdx.ref.parent.getItemIndex(x.classIdx.ref),
                                                x.nameIdx.ref.parent.getItemIndex(x.nameIdx.ref),
                                                x.protoIdx.ref.parent.getItemIndex(x.protoIdx.ref)), reverse=False)
        return method_id_item

    def initialize(self):
        self.add(self.getRoot().type_id_item_section.data[0], self.getRoot().proto_id_item_section.data[0], self.getRoot().string_id_item_section.data[0])
        self.add(self.getRoot().type_id_item_section.data[0], self.getRoot().proto_id_item_section.data[1], self.getRoot().string_id_item_section.data[7])
        self.add(self.getRoot().type_id_item_section.data[1], self.getRoot().proto_id_item_section.data[0], self.getRoot().string_id_item_section.data[0])