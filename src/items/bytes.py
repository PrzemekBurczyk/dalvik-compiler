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
        self.bytesCount = bytesCount
        self.value = value
        self.data = struct.pack(self.bytesCountMap.get(self.bytesCount), self.value)
    
    @staticmethod
    def getBytesArray(size):
        return [Bytes(1)] * size
