'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.class_def_item import ClassDefItem


class ClassDefItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

    def initialize(self):
        class_def_item = ClassDefItem(self)
        # class_def_item.classIdx.value = 0
        class_def_item.classIdx.ref_type = "index"
        class_def_item.classIdx.ref = self.getRoot().type_id_item_section.data[0]
        class_def_item.accessFlags.value = 1
        # class_def_item.superclassIdx.value = 1
        class_def_item.superclassIdx.ref_type = "index"
        class_def_item.superclassIdx.ref = self.getRoot().type_id_item_section.data[1]
        class_def_item.interfacesOff.value = 0
        # class_def_item.sourceFileIdx.value = 3
        class_def_item.sourceFileIdx.ref_type = "index"
        class_def_item.sourceFileIdx.ref = self.getRoot().string_id_item_section.data[3]
        class_def_item.annotationsOff.value = 0
        class_def_item.classDataOff.ref = self.getRoot().class_data_item_section.data[0]
        class_def_item.staticValuesOff.value = 0
        
        self.data.append(class_def_item)