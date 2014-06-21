'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.parser.measurable import Measurable


class CodeItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.registersSize = Bytes(self, 2)
        self.insSize = Bytes(self, 2)
        self.outsSize = Bytes(self, 2)
        self.triesSize = Bytes(self, 2)
        self.debugInfoOff = Bytes(self, 4)  # can it be 0 at all times?
        self.insnsSize = Bytes(self, 4)  # number of Bytes(self, 2) of instructions
        self.instructions = BytesArray(self, 0)

        self._data = [self.registersSize, self.insSize, self.outsSize, self.triesSize, self.debugInfoOff,
                      self.insnsSize, self.instructions]


class Instruction(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self._data = BytesArray(self, 0)
        
        
