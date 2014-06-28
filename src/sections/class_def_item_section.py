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
        
        class_def_item = ClassDefItem(self)
        class_def_item.classIdx = 0
        class_def_item.accessFlags = 1
        class_def_item.superclassIdx = 1
        class_def_item.interfacesOff = 0
        class_def_item.sourceFileIdx = 3
        class_def_item.annotationsOff = 0
        class_def_item.classDataOff = self.getRoot().class_data_item_section.data[0]
        class_def_item.staticValuesOff = 0
        
        self.data.append(class_def_item)