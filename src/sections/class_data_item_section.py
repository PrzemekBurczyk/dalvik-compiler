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
        
        class_data_item = ClassDataItem(self)
        class_data_item.staticFieldsSize.value = 0
        class_data_item.instanceFieldsSize.value = 0
        class_data_item.directMethodsSize.value = 2
        class_data_item.virtualMethodsSize.value = 0
        
        direct_method = DirectMethod(class_data_item)
        direct_method.fieldIdxDiff.value = 0
        byte = Bytes(direct_method, 1)
        byte.value = 0x4
        direct_method.accessFlags.data.append(byte)
        byte = Bytes(direct_method, 1)
        byte.value = 0x80
        direct_method.accessFlags.data.append(byte)
        byte = Bytes(direct_method, 1)
        byte.value = 0x81
        direct_method.accessFlags.data.append(byte)
        direct_method.codeOff.ref = self.getRoot().code_item_section.data[0]
        
        class_data_item.directMethods.append(direct_method)
        
        direct_method = DirectMethod(class_data_item)
        direct_method.fieldIdxDiff.value = 1
        direct_method.accessFlags.value = 9
        direct_method.codeOff.ref = self.getRoot().code_item_section.data[1]
        
        class_data_item.directMethods.append(direct_method)
        
        self.data.append(class_data_item)

        # are those two in section or in item?
        self.zeros = Bytes(self, 2)
        self.size = Bytes(self, 4)
        self.size.value = 0xc

        self._data + [self.zeros, self.size]

        # @property
        #def data(self):
        #    '''
        #    We shall watch out to keep additional fields at the end of _data probably
        #    '''
        #    return self._data + [self.zeros, self.size]
