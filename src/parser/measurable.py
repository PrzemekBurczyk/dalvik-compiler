'''
Created on 4 cze 2014

@author: Przemek
'''

from __builtin__ import type

import src.items


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
        print 'getItemIndex: ' + str(item)
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
        print "item: " + str(item)
        print type(item)
        return self.getIndexOffset(self.getItemIndex(item))

    def getGlobalOffset(self):
        return 0 if self.parent is None else self.parent.getItemOffset(self) + self.parent.getGlobalOffset()

    def getRoot(self):
        return self if self.parent is None else self.parent.getRoot()

    def getBytesCount(self):
        return len(self._data._data) if isinstance(self._data, src.items.bytes.Bytes) else sum(
            x.getBytesCount() if isinstance(x, Measurable) else len(x) for x in self._data)

    def printItemsOffset(self):
        print "self: " + str(self)
        if isinstance(self, src.items.bytes.Bytes) or isinstance(self, src.items.bytes_array.BytesArray):
            print "byte reached!"
            print self.getGlobalOffset()
        else:
            for item in self.data:
                item.printItemsOffset()


class BytesHaveNoItems(Exception):
    def __init__(self):
        pass


class ItemNotFound(Exception):
    def __init__(self):
        pass
    
    