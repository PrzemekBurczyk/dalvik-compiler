'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable
from src.items.class_data_item import ClassDataItem, DirectMethod
from src.items.bytes_array import BytesArray


class ClassDataItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        class_data_item = ClassDataItem(self)
        class_data_item.staticFieldsSize.value = 0
        class_data_item.instanceFieldsSize.value = 0
        class_data_item.directMethodsSize.value = 2
        class_data_item.virtualMethodsSize.value = 0
        
        direct_method = DirectMethod(class_data_item)
        direct_method.fieldIdxDiff.ref_type = "index"
        direct_method.fieldIdxDiff.ref = self.getRoot().method_id_item_section.data[0]
        direct_method.accessFlags.value = 0x10001
        direct_method.codeOff.ref = self.getRoot().code_item_section.data[0]
        class_data_item.directMethods.append(direct_method)
        
        direct_method = DirectMethod(class_data_item)
        direct_method.fieldIdxDiff.ref_type = "index"
        direct_method.fieldIdxDiff.ref = self.getRoot().method_id_item_section.data[1]
        direct_method.accessFlags.value = 0x9
        direct_method.codeOff.ref = self.getRoot().code_item_section.data[1]
        class_data_item.directMethods.append(direct_method)
        
        self.data.append(class_data_item)

        # zeros may be needed to have good alignment (to 4 bytes)
        self.zeros = Bytes(self, 2)

        #self._data + [self.size]
