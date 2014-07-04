'''
Created on 3 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.type_id_item import TypeIdItem


class TypeIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        item = TypeIdItem(self)
        item.data.value = 1
        self.data.append(item)
        item = TypeIdItem(self)
        item.data.value = 2
        self.data.append(item)
        item = TypeIdItem(self)
        item.data.value = 4
        self.data.append(item)
        item = TypeIdItem(self)
        item.data.value = 6
        self.data.append(item)
