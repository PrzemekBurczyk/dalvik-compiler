'''
Created on 4 cze 2014

@author: Przemek
'''

import src.items.bytes

class Mesaurable(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._data = []
        
    @property
    def data(self):
        return self._data
        
    def getItemOffset(self, index):
        if isinstance(self, src.items.bytes.Bytes):
            raise BytesHaveNoItems()
        return 0 if isinstance(self._data, src.items.bytes.Bytes) else sum([x.getBytesCount() if isinstance(x, Mesaurable) else len(x) for x in self._data[:index]])
    
    def getBytesCount(self):
        return len(self._data._data) if isinstance(self._data, src.items.bytes.Bytes) else sum(x.getBytesCount() if isinstance(x, Mesaurable) else len(x) for x in self._data)
    
class BytesHaveNoItems(Exception):
    
    def __init__(self):
        pass
    
    