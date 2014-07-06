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

    def add(self, shorty_idx, return_type_idx, parameters_off):
        proto_id_item = ProtoIdItem(self)
        proto_id_item.shorty_idx.ref_type = "index"
        proto_id_item.shorty_idx.ref = shorty_idx
        proto_id_item.return_type_idx.ref_type = "index"
        proto_id_item.return_type_idx.ref = return_type_idx
        proto_id_item.parameters_off.ref_type = "offset"
        proto_id_item.parameters_off.ref = parameters_off

        currentShortyIdx = shorty_idx.parent.getItemIndex(shorty_idx)
        currentReturnTypeIdx = return_type_idx.parent.getItemIndex(return_type_idx)
        currentParametersOff = parameters_off.parent.getItemIndex(parameters_off) if parameters_off is not None else None

        for item in self.data:
            existingShortyIdx = item.shorty_idx.ref.parent.getItemIndex(item.shorty_idx.ref)
            existingReturnTypeIdx = item.return_type_idx.ref.parent.getItemIndex(item.return_type_idx.ref)
            existingParametersOff = item.parameters_off.ref.parent.getItemIndex(item.parameters_off.ref) if item.parameters_off.ref is not None else None

            if currentShortyIdx == existingShortyIdx and currentReturnTypeIdx == existingReturnTypeIdx and currentParametersOff == existingParametersOff:
                return item

        self.data.append(proto_id_item)
        self.data.sort(cmp=None, key=lambda x: (x.return_type_idx.ref.parent.getItemIndex(x.return_type_idx.ref),
                                                x.parameters_off.ref.parent.getItemIndex(x.parameters_off.ref) if x.parameters_off.ref is not None else 0), reverse=False)
        return proto_id_item

    def initialize(self):
        self.add(self.getRoot().string_id_item_section.data[4], self.getRoot().type_id_item_section.data[2], None)
        self.add(self.getRoot().string_id_item_section.data[5], self.getRoot().type_id_item_section.data[2], self.getRoot().type_list_section.data[0])