'''
Created on 4 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable
from src.parser.reference import Reference


class BytesArray(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent, size):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self._data = [Bytes(self, 1)] * size


class ULeb128(BytesArray, Reference):

    def __init__(self, parent):
        BytesArray.__init__(self, parent, 0)
        Reference.__init__(self)
        self.low_order_mask = 0b01111111
        self.high_order_mask = 0b10000000
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.setValue(value)

    def setValue(self, value):
        byte = self.low_order_mask & value
        value >>= 7
        if value != 0:
            byte |= self.high_order_mask
        self._data.append(Bytes(self, 1, byte))
        if value != 0:
            self.setValue(value)
