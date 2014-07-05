'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.parser.measurable import Measurable


class DebugInfoItemSection(Measurable):
    '''
    Is it needed?
    For sure!
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        bytes_array = BytesArray(self, 11)
        bytes_array.data[0] = Bytes(bytes_array, 1, 0x1)
        bytes_array.data[1] = Bytes(bytes_array, 1, 0)
        bytes_array.data[2] = Bytes(bytes_array, 1, 0x7)
        bytes_array.data[3] = Bytes(bytes_array, 1, 0xe)
        bytes_array.data[4] = Bytes(bytes_array, 1, 0)
        bytes_array.data[5] = Bytes(bytes_array, 1, 0x3)
        bytes_array.data[6] = Bytes(bytes_array, 1, 0x1)
        bytes_array.data[7] = Bytes(bytes_array, 1, 0)
        bytes_array.data[8] = Bytes(bytes_array, 1, 0x7)
        bytes_array.data[9] = Bytes(bytes_array, 1, 0xe)
        bytes_array.data[10] = Bytes(bytes_array, 1, 0)

        self.data.append(bytes_array)