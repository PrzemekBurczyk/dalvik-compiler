'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.type_list import TypeList


class TypeListSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        # it holds Bytes(self, 2) between it's items! no zero bytes at the end!
        
        type_list = TypeList(self)
        type_list.size = 1
        type_list.typeIdItem = 3
        self.data.append(type_list)