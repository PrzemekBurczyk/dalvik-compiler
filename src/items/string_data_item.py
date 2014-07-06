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

    def __init__(self, parent, string=""):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        self.utf16Size = Bytes(self, 1)
        self.string = BytesArray(self, 0)  # it is data from dump, but name is already reserved
        self.rawString = string
        self._data = [self.utf16Size, self.string, self.rawString]
        self.rawString = string
        self.setString(string)

    def setString(self, string):
        '''
        Fills in self.string BytesArray
        '''
        if isinstance(string, basestring):
            self.utf16Size.value = string.__len__()
            for x in string:
                byte = Bytes(self.string, 1)
                byte.value = int(x.encode('hex'), 16)
                self.string.data.append(byte)
            self.string.data.append(Bytes(self.string, 1))
            