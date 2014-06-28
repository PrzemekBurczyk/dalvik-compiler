'''
Created on 4 cze 2014

@author: Przemek
'''

from __builtin__ import type

import src.items
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
        return len(self._data._data) if isinstance(self._data, src.items.bytes.Bytes) else sum(x.getBytesCount() if isinstance(x, Measurable) else len(x) for x in self._data)

    def printItem(self, output):
        print self
        if isinstance(self, src.items.bytes.Bytes):
            if self.ref is not None:
                if self.ref == 0:
                    self.value = 0
                else:
                    self.value = self.ref.getGlobalOffset()
            output.write(self.data)
        elif isinstance(self, src.items.bytes_array.BytesArray):
            for byte in self.data:
                output.write(byte.data)
        elif isinstance(self.data, src.items.bytes.Bytes):
            if self.data.ref is not None:
                if self.data.ref == 0:
                    self.data.value = 0
                else:
                    self.data.value = self.data.ref.getGlobalOffset()
            output.write(self.data.data)
        elif isinstance(self.data, src.items.bytes_array.BytesArray):
            for byte in self.data:
                if byte.ref is not None:
                    if byte.ref == 0:
                        byte.value = 0;
                    else:
                        byte.value = byte.ref.getGlobalOffset()
                output.write(byte.data)
        else:
            for item in self.data:
                item.printItem(output)

class BytesHaveNoItems(Exception):
    def __init__(self):
        pass


class ItemNotFound(Exception):
    def __init__(self):
        pass
    
    