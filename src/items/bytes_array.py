'''
Created on 4 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.mesaurable import Mesaurable


class BytesArray(Mesaurable):
    '''
    classdocs
    '''


    def __init__(self, parent, size):
        '''
        Constructor
        '''
        Mesaurable.__init__(self, parent)
        
        self._data = [Bytes(self, 1)] * size
        
        