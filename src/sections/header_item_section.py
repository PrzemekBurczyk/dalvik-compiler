'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.header_item import HeaderItem
from src.parser.measurable import Measurable

class HeaderItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        self.headerItem = HeaderItem(self)