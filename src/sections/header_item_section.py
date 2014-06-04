'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.header_item import HeaderItem
from src.parser.mesaurable import Mesaurable


class HeaderItemSection(Mesaurable):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Mesaurable.__init__(self)
        
        self.headerItem = HeaderItem()