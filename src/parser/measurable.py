'''
Created on 4 cze 2014

@author: Przemek
'''

from __builtin__ import type

import src.items
import src.parser
import src.sections


class Measurable(object):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        # print "mesaurable parent: " + str(parent)
        self._parent = parent
        self._data = []

    @property
    def data(self):
        return self._data

    @property
    def parent(self):
        return self._parent

    def getIndexOffset(self, index):
        if isinstance(self, src.items.bytes.Bytes) or isinstance(self, src.items.bytes_array.BytesArray):
            raise BytesHaveNoItems()
        return 0 if isinstance(self._data, src.items.bytes.Bytes) or isinstance(self, src.items.bytes_array.BytesArray) else sum([x.getBytesCount() if isinstance(x, Measurable) else len(x) for x in self._data[:index]])

    def getItemIndex(self, item):
        if isinstance(self, src.items.bytes.Bytes) or isinstance(self, src.items.bytes_array.BytesArray):
            raise BytesHaveNoItems()
        if isinstance(self._data, src.items.bytes.Bytes) or isinstance(self._data, src.items.bytes_array.BytesArray):
            raise ItemNotFound()
        try:
            index = self._data.index(item)
            return index
        except ValueError:
            raise ItemNotFound()

    def getItemOffset(self, item):
        return self.getIndexOffset(self.getItemIndex(item))

    def getGlobalOffset(self):
        return 0 if self.parent is None else self.parent.getItemOffset(self) + self.parent.getGlobalOffset()

    def getRoot(self):
        return self if self.parent is None else self.parent.getRoot()

    def getBytesCount(self):
        if isinstance(self._data, src.items.bytes.Bytes) or isinstance(self._data, src.items.bytes_array.BytesArray):
            return len(self._data._data)
        else:
            bytesSum = sum(x.getBytesCount() if isinstance(x, Measurable) else sum(map(lambda y: y.getBytesCount() if isinstance(y, Measurable) else len(y), x)) for x in self._data)
            return bytesSum

    def printItem(self, output):
        if isinstance(self, src.parser.dex.Dex):
            # self.header_item_section[0].checksum =
            # self.header_item_section[0].signature =
            self.header_item_section.data[0].data_size.value = self.header_item_section.getDataSize()
            if self.header_item_section.data[0].data_size.value % 4 != 0:
                print "HEADER_ITEM.DATA_SIZE SHOULD BE ALIGNED TO 4 BYTES! while it is " + str(self.header_item_section.data[0].data_size.value)
        if isinstance(self, src.items.bytes.Bytes):
            if self.ref is not None:
                if self.ref == 0:
                    self.value = 0
                elif self.ref_type == "offset":
                    self.value = self.ref.getGlobalOffset()
                else:
                    self.value = self.ref.parent.getItemIndex(self.ref)
            output.write(self.data)
        elif isinstance(self, src.items.bytes_array.BytesArray):
            for byte in self.data:
                output.write(byte.data)
        elif isinstance(self.data, src.items.bytes.Bytes):
            if self.data.ref is not None:
                if self.data.ref == 0:
                    self.data.value = 0
                elif self.data.ref_type == "offset":
                    self.data.value = self.data.ref.getGlobalOffset()
                else:
                    self.data.value = self.data.ref.parent.getItemIndex(self.data.ref)
            output.write(self.data.data)
        elif isinstance(self.data, src.items.bytes_array.BytesArray):
            for byte in self.data.data:
                if byte.ref is not None:
                    if byte.ref == 0:
                        byte.value = 0
                    elif byte.ref_type == "offset":
                        byte.value = byte.ref.getGlobalOffset()
                    else:
                        byte.value = byte.parent.getItemIndex(byte.ref)
                output.write(byte.data)
        else:
            for item in self.data:
                if isinstance(item, list):
                    for subitem in item:
                        subitem.printItem(output)
                else:
                    item.printItem(output)


class BytesHaveNoItems(Exception):
    def __init__(self):
        pass


class ItemNotFound(Exception):
    def __init__(self):
        pass