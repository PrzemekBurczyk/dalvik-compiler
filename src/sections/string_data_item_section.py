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
        self.data.append(StringDataItem(self, "<init>"))
        self.data.append(StringDataItem(self, "LMain;"))
        self.data.append(StringDataItem(self, "Ljava/lang/Object;"))
        self.data.append(StringDataItem(self, "Main.java"))
        self.data.append(StringDataItem(self, "V"))
        self.data.append(StringDataItem(self, "VL"))
        self.data.append(StringDataItem(self, "[Ljava/lang/String;"))
        self.data.append(StringDataItem(self, "main"))
