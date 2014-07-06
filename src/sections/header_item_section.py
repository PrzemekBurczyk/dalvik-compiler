'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.items.header_item import HeaderItem
from src.parser.measurable import Measurable


class HeaderItemSection(Measurable):
    '''
    classdocs
    '''

    def getDataSize(self):
        return sum(x.getBytesCount() for x in self.getRoot().data[7:])

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        header_item = HeaderItem(self)

        header_item.magic.data[0] = Bytes(header_item, 1, 0x64)
        header_item.magic.data[1] = Bytes(header_item, 1, 0x65)
        header_item.magic.data[2] = Bytes(header_item, 1, 0x78)
        header_item.magic.data[3] = Bytes(header_item, 1, 0x0a)
        header_item.magic.data[4] = Bytes(header_item, 1, 0x30)
        header_item.magic.data[5] = Bytes(header_item, 1, 0x33)
        header_item.magic.data[6] = Bytes(header_item, 1, 0x35)
        header_item.magic.data[7] = Bytes(header_item, 1, 0x00)

        header_item.header_size.value = 0x70
        header_item.endian_tag.value = 0x12345678
        header_item.link_size.value = 0
        header_item.link_offset.value = 0
        header_item.map_off.ref = self.getRoot().map_item_section
        header_item.string_ids_size.value = 8
        header_item.string_ids_off.ref = self.getRoot().string_id_item_section
        header_item.type_ids_size.value = 4
        header_item.type_ids_off.ref = self.getRoot().type_id_item_section
        header_item.proto_ids_size.value = 2
        header_item.proto_ids_off.ref = self.getRoot().proto_id_item_section
        header_item.field_ids_size.value = 0
        # header_item.field_ids_off.ref = self.getRoot().field_id_item_section
        header_item.method_ids_size.value = 3
        header_item.method_ids_off.ref = self.getRoot().method_id_item_section
        header_item.class_defs_size.value = 1
        header_item.class_defs_off.ref = self.getRoot().class_def_item_section
        header_item.data_off.ref = self.getRoot().code_item_section

        self.data.append(header_item)
