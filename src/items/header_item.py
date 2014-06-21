'''
Created on 3 cze 2014

@author: Przemek
'''
import hashlib

from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.parser.measurable import Measurable


class HeaderItem(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.magic = Bytes(self, 8)
        self.checksum = Bytes(self, 4)
        self.signature = BytesArray(self, 20)
        self.file_size = Bytes(self, 4)
        self.header_size = Bytes(self, 4)
        self.endian_tag = Bytes(self, 4)
        self.link_size = Bytes(self, 4)
        self.link_offset = Bytes(self, 4)
        self.map_off = Bytes(self, 4)
        self.string_ids_size = Bytes(self, 4)
        self.string_ids_off = Bytes(self, 4)
        self.type_ids_size = Bytes(self, 4)
        self.type_ids_off = Bytes(self, 4)
        self.proto_ids_size = Bytes(self, 4)
        self.proto_ids_off = Bytes(self, 4)
        self.field_ids_size = Bytes(self, 4)
        self.field_ids_off = Bytes(self, 4)
        self.method_ids_size = Bytes(self, 4)
        self.method_ids_off = Bytes(self, 4)
        self.class_defs_size = Bytes(self, 4)
        self.class_defs_off = Bytes(self, 4)
        self.data_size = Bytes(self, 4)
        self.data_off = Bytes(self, 4)

        self._data = [self.magic, self.checksum, self.signature, self.file_size, self.header_size, self.endian_tag,
                      self.link_size,
                      self.link_offset, self.map_off, self.string_ids_size, self.string_ids_off, self.type_ids_size,
                      self.type_ids_off,
                      self.proto_ids_size, self.proto_ids_off, self.field_ids_size, self.field_ids_off,
                      self.method_ids_size,
                      self.method_ids_off, self.class_defs_size, self.class_defs_off, self.data_size, self.data_off]

    def calculateSha1(self, data):
        sha1 = hashlib.sha1()
        sha1.update(data)
        return hash.digest()
