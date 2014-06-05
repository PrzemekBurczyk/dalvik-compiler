import struct

from src.parser.measurable import Measurable

class Bytes(Measurable):

    def __init__(self, parent, bytesCount, value=0):
        '''
        B 1 byte unsigned
        H 2 bytes unsigned
        I 4 bytes unsigned
        Q 8 bytes unsigned
        '''
        Measurable.__init__(self, parent)
        
        self.bytesCountMap = {1: 'B', 2: 'H', 4: 'I', 8: 'Q'}
        if not self.bytesCountMap.has_key(bytesCount):
            raise InappropriateBytesCount()
        
        self._bytesCount = bytesCount
        self._value = value
        self._data = struct.pack(self.bytesCountMap.get(self._bytesCount), self._value)
        
    @property
    def bytesCount(self):
        return self._bytesCount
    
    @bytesCount.setter
    def bytesCount(self, bytesCount):
        if not self.bytesCountMap.has_key(bytesCount):
            raise InappropriateBytesCount()
        self._data = struct.pack(self.bytesCountMap.get(bytesCount), struct.unpack(self.bytesCountMap.get(self._bytesCount), self._data)[0]) # 0 because it is a tuple
        self._bytesCount = bytesCount
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value
        self._data = struct.pack(self.bytesCountMap.get(self._bytesCount), self._value)

class InappropriateBytesCount(Exception):
    
    def __init__(self):
        pass