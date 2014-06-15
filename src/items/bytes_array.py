'''
Created on 4 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


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
        
        