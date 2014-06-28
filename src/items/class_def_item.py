'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class ClassDefItem(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.classIdx = Bytes(self, 4)
        self.accessFlags = Bytes(self, 4)
        self.superclassIdx = Bytes(self, 4)
        self.interfacesOff = Bytes(self, 4)
        self.sourceFileIdx = Bytes(self, 4)
        self.annotationsOff = Bytes(self, 4)
        self.classDataOff = Bytes(self, 4)
        self.staticValuesOff = Bytes(self, 4)

        self._data = [self.classIdx, self.accessFlags, self.superclassIdx, self.interfacesOff, self.sourceFileIdx,
                      self.annotationsOff,
                      self.classDataOff, self.staticValuesOff]
        