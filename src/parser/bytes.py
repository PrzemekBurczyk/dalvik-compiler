import struct

class Bytes(object):

    def __init__(self, bytesCount, value=0):
        '''
        B 1 byte unsigned
        H 2 bytes unsigned
        I 4 bytes unsigned
        Q 8 bytes unsigned
        '''
        self.bytesCountMap = {1: 'B', 2: 'H', 4: 'I', 8: 'Q'}
        self.bytesCount = bytesCount
        self.value = value
        
    def getBinary(self):
        return struct.pack(self.bytesCountMap.get(self.bytesCount), self.value)
        