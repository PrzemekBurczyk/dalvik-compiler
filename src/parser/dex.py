'''
Created on 3 cze 2014

@author: Przemek
'''
from sections.class_data_item_section import ClassDataItemSection
from sections.class_def_item_section import ClassDefItemSection
from sections.code_item_section import CodeItemSection
from sections.debug_info_item_section import DebugInfoItemSection
from sections.header_item_section import HeaderItemSection
from sections.map_item_section import MapItemSection
from sections.method_id_item_section import MethodIdItemSection
from sections.proto_id_item_section import ProtoIdItemSection
from sections.string_data_item_section import StringDataItemSection
from sections.string_id_item_section import StringIdItemSection
from sections.type_id_item_section import TypeIdItemSection
from sections.type_list_section import TypeListSection
from src.parser.measurable import Measurable


class Dex(Measurable):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Measurable.__init__(self, None) # Dex is the root
        
        self.header_item_section = HeaderItemSection(self)
        self.string_id_item_section = StringIdItemSection(self)
        self.type_id_item_section = TypeIdItemSection(self)
        self.proto_id_item_section = ProtoIdItemSection(self)
        self.method_id_item_section = MethodIdItemSection(self)
        self.class_def_item_section = ClassDefItemSection(self)
        self.code_item_section = CodeItemSection(self)
        self.type_list_section = TypeListSection(self)
        self.string_data_item_section = StringDataItemSection(self)
        self.debug_info_item_section = DebugInfoItemSection(self)
        self.class_data_item_section = ClassDataItemSection(self)
        self.map_item_section = MapItemSection(self)
        
        self._data = [self.header_item_section, self.string_id_item_section, self.type_id_item_section,
                      self.proto_id_item_section, self.method_id_item_section, self.class_def_item_section,
                      self.code_item_section, self.type_list_section, self.string_data_item_section,
                      self.debug_info_item_section, self.class_data_item_section,self.map_item_section]