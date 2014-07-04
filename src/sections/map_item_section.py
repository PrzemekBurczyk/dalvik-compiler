'''
Created on 5 cze 2014

@author: Przemek
'''

from src.parser.measurable import Measurable
from src.items.map_item import MapItem


class MapItemSection(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        #0
        map_item = MapItem(self)
        map_item.type.value = 0
        map_item.unused.value = 0
        map_item.size.value = 1
        map_item.offset.ref = 0
        
        self.data.append(map_item)

        #1
        map_item = MapItem(self)
        map_item.type.value = 1
        map_item.unused.value = 0
        map_item.size.value = 8
        map_item.offset.ref = self.getRoot().string_data_item_section.data[0]
        
        self.data.append(map_item)
        
        #2
        map_item = MapItem(self)
        map_item.type.value = 2
        map_item.unused.value = 0
        map_item.size.value = 4
        map_item.offset.ref = self.getRoot().type_list_section.data[0]
        
        self.data.append(map_item)
        
        #3
        map_item = MapItem(self)
        map_item.type.value = 3
        map_item.unused.value = 0
        map_item.size.value = 2
        map_item.offset.ref = self.getRoot().proto_id_item_section.data[0]
        
        self.data.append(map_item)
        
        #4
        map_item = MapItem(self)
        map_item.type.value = 5
        map_item.unused.value = 0
        map_item.size.value = 3
        map_item.offset.ref = self.getRoot().method_id_item_section.data[0]
        
        self.data.append(map_item)
        
        #5
        map_item = MapItem(self)
        map_item.type.value = 6
        map_item.unused.value = 0
        map_item.size.value = 1
        map_item.offset.ref = self.getRoot().class_def_item_section.data[0]
        
        self.data.append(map_item)
        
        #6
        map_item = MapItem(self)
        map_item.type.value = 0x2001
        map_item.unused.value = 0
        map_item.size.value = 2
        map_item.offset.ref = self.getRoot().code_item_section.data[0]
        
        self.data.append(map_item)
        
        #7
        map_item = MapItem(self)
        map_item.type.value = 0x1001
        map_item.unused.value = 0
        map_item.size.value = 1
        map_item.offset.ref = self.getRoot().type_list_section.data[0]
        
        self.data.append(map_item)
        
        #8
        map_item = MapItem(self)
        map_item.type.value = 0x2002
        map_item.unused.value = 0
        map_item.size.value = 8
        map_item.offset.ref = self.getRoot().string_data_item_section.data[0]
        
        self.data.append(map_item)
        
        #9
        map_item = MapItem(self)
        map_item.type.value = 0x2003
        map_item.unused.value = 0
        map_item.size.value = 2
        map_item.offset.ref = 0
        
        self.data.append(map_item)
        
        #10
        map_item = MapItem(self)
        map_item.type.value = 0x2000
        map_item.unused.value = 0
        map_item.size.value = 1
        map_item.offset.ref = self.getRoot().class_data_item_section.data[0]
        
        self.data.append(map_item)
        
        #11    
        map_item = MapItem(self)
        map_item.type.value = 0x1000
        map_item.unused.value = 0
        map_item.size.value = 1
        map_item.offset.ref = self
        
        self.data.append(map_item)