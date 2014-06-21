'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class ClassDataItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        # are those two in section or in item?
        self.zeros = Bytes(self, 2)
        self.size = Bytes(self, 4)

        self._data + [self.zeros, self.size]

        # @property
        #def data(self):
        #    '''
        #    We shall watch out to keep additional fields at the end of _data probably
        #    '''
        #    return self._data + [self.zeros, self.size]
