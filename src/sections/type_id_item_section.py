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
        #item = TypeIdItem(self)
        # item.data.value = 1
        #item.data.ref_type = "index"
        #item.data.ref = self.getRoot().string_id_item_section.data[1]
        #self.data.append(item)
        #item = TypeIdItem(self)
        # item.data.value = 2
        #item.data.ref_type = "index"
        #item.data.ref = self.getRoot().string_id_item_section.data[2]
        #self.data.append(item)
        #item = TypeIdItem(self)
        # item.data.value = 4
        #item.data.ref_type = "index"
        #item.data.ref = self.getRoot().string_id_item_section.data[4]
        #self.data.append(item)
        #item = TypeIdItem(self)
        # item.data.value = 6
        #item.data.ref_type = "index"
        #item.data.ref = self.getRoot().string_id_item_section.data[6]
        #self.data.append(item)
        
        self.addTypeIdItemAndSort("LMain;");
        self.addTypeIdItemAndSort("Ljava/lang/Object;");
        self.addTypeIdItemAndSort("V");
        self.addTypeIdItemAndSort("[Ljava/lang/String;");
        
    def addTypeIdItemAndSort(self, typeStringName):
        string_id = 0
        for x in self.getRoot().string_data_item_section.data:
            if x.rawString == typeStringName:
                string_id = self.getRoot().string_data_item_section.data.index(x)
        
        item = TypeIdItem(self)
        item.data.ref_type = "index"
        item.data.ref = self.getRoot().string_id_item_section.data[string_id]
        self.data.append(item)
        
        
        #if len(self.data):
        #    self.data.sort(cmp=None, key=lambda x: x.getStringIndex(), reverse=False)
        
