'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.parser.measurable import Measurable


class StringDataItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        self.utf16Size = Bytes(self, 1)
        self.string = BytesArray(self, 0) #it is data from dump, but name is already reserved
        
        self._data = [self.utf16Size, self.string]