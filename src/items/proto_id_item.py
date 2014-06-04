'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.mesaurable import Mesaurable


class ProtoIdItem(Mesaurable):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Mesaurable.__init__(self)
        
        self.shorty_idx = Bytes(4)
        self.return_type_idx = Bytes(4)
        self.parameters_off = Bytes(4)