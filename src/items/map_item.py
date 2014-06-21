'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class MapItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.type = Bytes(self, 2)
        self.unused = Bytes(self, 2)
        self.size = Bytes(self, 4)
        self.offset = Bytes(self, 4)

        self._data = [self.type, self.unused, self.size, self.offset]
        