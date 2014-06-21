'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class ProtoIdItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.shorty_idx = Bytes(self, 4)
        self.return_type_idx = Bytes(self, 4)
        self.parameters_off = Bytes(self, 4)

        self._data = [self.shorty_idx, self.return_type_idx, self.parameters_off]