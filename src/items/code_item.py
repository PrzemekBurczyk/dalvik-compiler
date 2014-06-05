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
        self.debugInfoOff = Bytes(self, 4)
        self.insnsSize = Bytes(self, 4) #number of Bytes(self, 2) of instructions
        self.instructions = BytesArray(self, 0)
        
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
        
        
