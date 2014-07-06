'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.string_data_item import StringDataItem
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
        
    def initialize(self):
        pass

    def addAndSortStrings(self, stringToAdd):
        self.data.append(StringDataItem(self, stringToAdd))
        if len(self.data):
            self.data.sort(cmp=None, key=lambda x: x.rawString, reverse=False)

        #print "---StringDataItemSection data:"
        #for x in self.data:
        #    print x.rawString
        #print "---end of strinfDataItemSection"