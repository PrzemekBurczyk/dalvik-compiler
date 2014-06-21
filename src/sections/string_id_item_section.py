'''
Created on 3 cze 2014

@author: Przemek
'''
from src.items.string_id_item import StringIdItem
from src.parser.measurable import Measurable


class StringIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        for i in self.getRoot().string_data_item_section.data:
            item = StringIdItem(self)
            item.data.ref = i
            self.data.append(item)
