'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.string_id_item import StringIdItem
from src.parser.measurable import Measurable


class TypeIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        item = StringIdItem(self)
        item.data.value = 1
        self.data.append(item)
        item = StringIdItem(self)
        item.data.value = 2
        self.data.append(item)
        item = StringIdItem(self)
        item.data.value = 4
        self.data.append(item)
        item = StringIdItem(self)
        item.data.value = 6
        self.data.append(item)
