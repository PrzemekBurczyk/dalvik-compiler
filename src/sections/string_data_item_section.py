'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable


class StringDataItemSection(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)