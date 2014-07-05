'''
Created on 4 cze 2014

@author: Przemek
'''

from __builtin__ import type
import zlib
import hashlib

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

    def getChecksum(self, buf):
        if isinstance(self, src.items.bytes.Bytes):
            if self.ref is not None:
                if self.ref == 0:
                    self.value = 0
                elif self.ref_type == "offset":
                    self.value = self.ref.getGlobalOffset()
                else:
                    self.value = self.ref.parent.getItemIndex(self.ref)
            buf.append(self.data)
        elif isinstance(self, src.items.bytes_array.BytesArray):
            for byte in self.data:
                buf.append(byte.data)
        elif isinstance(self.data, src.items.bytes.Bytes):
            if self.data.ref is not None:
                if self.data.ref == 0:
                    self.data.value = 0
                elif self.data.ref_type == "offset":
                    self.data.value = self.data.ref.getGlobalOffset()
                else:
                    self.data.value = self.data.ref.parent.getItemIndex(self.data.ref)
            buf.append(self.data.data)
        elif isinstance(self.data, src.items.bytes_array.BytesArray):
            for byte in self.data.data:
                if byte.ref is not None:
                    if byte.ref == 0:
                        byte.value = 0
                    elif byte.ref_type == "offset":
                        byte.value = byte.ref.getGlobalOffset()
                    else:
                        byte.value = byte.parent.getItemIndex(byte.ref)
                buf.append(byte.data)
        else:
            if isinstance(self, src.items.header_item.HeaderItem):
                for item in self.data[2:]:  # omit magic and checksum
                    if isinstance(item, list):
                        for subitem in item:
                            subitem.getChecksum(buf)
                    else:
                        item.getChecksum(buf)
            else:
                for item in self.data:
                    if isinstance(item, list):
                        for subitem in item:
                            subitem.getChecksum(buf)
                    else:
                        item.getChecksum(buf)

    def getSignature(self, sha1):
        if isinstance(self, src.items.bytes.Bytes):
            if self.ref is not None:
                if self.ref == 0:
                    self.value = 0
                elif self.ref_type == "offset":
                    self.value = self.ref.getGlobalOffset()
                else:
                    self.value = self.ref.parent.getItemIndex(self.ref)
            sha1.update(self.data)
        elif isinstance(self, src.items.bytes_array.BytesArray):
            for byte in self.data:
                sha1.update(byte.data)
        elif isinstance(self.data, src.items.bytes.Bytes):
            if self.data.ref is not None:
                if self.data.ref == 0:
                    self.data.value = 0
                elif self.data.ref_type == "offset":
                    self.data.value = self.data.ref.getGlobalOffset()
                else:
                    self.data.value = self.data.ref.parent.getItemIndex(self.data.ref)
            sha1.update(self.data.data)
        elif isinstance(self.data, src.items.bytes_array.BytesArray):
            for byte in self.data.data:
                if byte.ref is not None:
                    if byte.ref == 0:
                        byte.value = 0
                    elif byte.ref_type == "offset":
                        byte.value = byte.ref.getGlobalOffset()
                    else:
                        byte.value = byte.parent.getItemIndex(byte.ref)
                sha1.update(byte.data)
        else:
            if isinstance(self, src.items.header_item.HeaderItem):
                for item in self.data[3:]:  # omit magic, checksum and signature
                    if isinstance(item, list):
                        for subitem in item:
                            subitem.getSignature(sha1)
                    else:
                        item.getSignature(sha1)
            else:
                for item in self.data:
                    if isinstance(item, list):
                        for subitem in item:
                            subitem.getSignature(sha1)
                    else:
                        item.getSignature(sha1)

    def printItem(self, output):
        if isinstance(self, src.parser.dex.Dex):
            sha1 = hashlib.sha1()
            self.getSignature(sha1)
            digest = sha1.digest()
            for i in range(20):
                self.header_item_section.data[0].signature.data[i] = src.items.bytes.Bytes(self.header_item_section.data[0].signature, 1, int(digest[i].encode('hex'), 16))

            buf = []
            self.getChecksum(buf)
            self.header_item_section.data[0].checksum.value = zlib.adler32("".join(buf))

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