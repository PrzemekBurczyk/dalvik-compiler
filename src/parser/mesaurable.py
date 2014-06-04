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
        self.data = []
        
    def getItemOffset(self, index):
        return index if isinstance(self.data, src.items.bytes.Bytes) else sum([x.getBytesCount() if isinstance(x, Mesaurable) else len(x) for x in self.data[:index]])
    
    def getBytesCount(self):
        return len(self.data) if isinstance(self.data, src.items.bytes.Bytes) else sum(x.getBytesCount() if isinstance(x, Mesaurable) else len(x) for x in self.data)
    
    
    
    