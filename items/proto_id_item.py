'''
Created on 3 cze 2014

@author: Przemek
'''
from parser.bytes import Bytes

class ProtoIdItem(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.shorty_idx = Bytes(4)
        self.return_type_idx = Bytes(4)
        self.parameters_off = Bytes(4)