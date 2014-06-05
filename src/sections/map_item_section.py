'''
Created on 5 cze 2014

@author: Przemek
'''

from src.parser.mesaurable import Mesaurable


class MapItemSection(Mesaurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        
        Mesaurable.__init__(self, parent)
