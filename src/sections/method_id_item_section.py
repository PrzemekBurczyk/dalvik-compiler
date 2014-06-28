'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.method_id_item import MethodIdItem


class MethodIdItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        method_id_item = MethodIdItem(self)
        method_id_item.classIdx = 0
        method_id_item.protoIdx = 0
        method_id_item.nameIdx = 0
        self.data.append(method_id_item)
        
        method_id_item = MethodIdItem(self)
        method_id_item.classIdx = 0
        method_id_item.protoIdx = 1
        method_id_item.nameIdx = 7
        self.data.append(method_id_item)
        
        method_id_item = MethodIdItem(self)
        method_id_item.classIdx = 1
        method_id_item.protoIdx = 0
        method_id_item.nameIdx = 0
        self.data.append(method_id_item)