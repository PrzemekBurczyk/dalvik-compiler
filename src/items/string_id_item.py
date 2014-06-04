'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.mesaurable import Mesaurable


class StringIdItem(Mesaurable):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Mesaurable.__init__(self)
        
        self._data = Bytes(4)