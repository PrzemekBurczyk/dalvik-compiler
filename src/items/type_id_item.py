'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.mesaurable import Mesaurable


class TypeIdItem(Mesaurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Mesaurable.__init__(self, parent)
        
        self._data = Bytes(self, 4)