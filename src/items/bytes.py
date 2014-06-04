import struct

from src.parser.mesaurable import Mesaurable

class Bytes(Mesaurable):

    def __init__(self, bytesCount, value=0):
        '''
        B 1 byte unsigned
        H 2 bytes unsigned
        I 4 bytes unsigned
        Q 8 bytes unsigned
        '''
        Mesaurable.__init__(self)
        
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
    
    @staticmethod
    def getBytesArray(size):
        '''
        It is vital to remember not to create arrays of Bytes(x) where x > 1, they will not be handled properly
        '''
        return [Bytes(1)] * size

class InappropriateBytesCount(Exception):
    
    def __init__(self):
        pass