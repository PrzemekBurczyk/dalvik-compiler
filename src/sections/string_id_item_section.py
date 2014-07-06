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
    
    def initialize(self):
        pass

    def addStringIdItem(self, string_data_item):
        item = StringIdItem(self)
        item.data.ref = string_data_item
        self.data.append(item)
        
        if len(self.data):
            self.data.sort(cmp=None, key=lambda x: x.data.ref.rawString, reverse=False)
        
        #print "refs from string_id_item sections:"
        #for item in self.data:
        #    print item.data.ref.rawString
        
