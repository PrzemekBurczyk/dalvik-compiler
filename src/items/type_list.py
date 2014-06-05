'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class TypeList(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        self.size = Bytes(self, 4)
        self.typeIdItem = Bytes(self, 2)
        self.zeros = Bytes(self, 2) #the last item in parent's list doesn't have those zeros, it might be a cause of errors!