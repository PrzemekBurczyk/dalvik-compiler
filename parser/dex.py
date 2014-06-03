'''
Created on 3 cze 2014

@author: Przemek
'''
from sections.header_item_section import HeaderItemSection
from sections.proto_id_item_section import ProtoIdItemSection
from sections.string_id_item_section import StringIdItemSection
from sections.type_id_item_section import TypeIdItemSection


class Dex(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.header_item_section = HeaderItemSection()
        self.string_id_item_section = StringIdItemSection()
        self.type_id_item_section = TypeIdItemSection()
        self.proto_id_item_section = ProtoIdItemSection()