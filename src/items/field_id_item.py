'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class FieldIdItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        self.classIdx = Bytes(self, 2)
        self.returnTypeIdx = Bytes(self, 2)
        self.nameIdx = Bytes(self, 4)
        
        self._data = [self.classIdx, self.returnTypeIdx, self.nameIdx]