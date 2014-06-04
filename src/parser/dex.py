'''
Created on 3 cze 2014

@author: Przemek
'''
from sections.header_item_section import HeaderItemSection
from sections.proto_id_item_section import ProtoIdItemSection
from sections.string_id_item_section import StringIdItemSection
from sections.type_id_item_section import TypeIdItemSection
from src.parser.mesaurable import Mesaurable


class Dex(Mesaurable):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Mesaurable.__init__(self, None) # Dex is the root
        
        self.header_item_section = HeaderItemSection(self)
        self.string_id_item_section = StringIdItemSection(self)
        self.type_id_item_section = TypeIdItemSection(self)
        self.proto_id_item_section = ProtoIdItemSection(self)