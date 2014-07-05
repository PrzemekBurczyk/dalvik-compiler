'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable
from src.items.bytes_array import BytesArray, ULeb128


class ClassDataItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.staticFieldsSize = ULeb128(self)
        self.instanceFieldsSize = ULeb128(self)
        self.directMethodsSize = ULeb128(self)
        self.virtualMethodsSize = ULeb128(self)
        self.staticFields = []
        self.instanceFields = []
        self.directMethods = []
        self.virtualMethods = []

        self._data = [self.staticFieldsSize, self.instanceFieldsSize, self.directMethodsSize, self.virtualMethodsSize,
                      self.staticFields, self.instanceFields, self.directMethods, self.virtualMethods]


class Member(Measurable):
    def __init__(self, parent):
        Measurable.__init__(self, parent)
        self.fieldIdxDiff = ULeb128(self)
        self.accessFlags = ULeb128(self)

        self._data = [self.fieldIdxDiff, self.accessFlags]


class StaticField(Member):
    def __init__(self, parent):
        Member.__init__(self, parent)
        # didn't see one, need to check maybe


class InstanceField(Member):
    def __init__(self, parent):
        Member.__init__(self, parent)


class Method(Member):
    def __init__(self, parent):
        '''
        accessFlags is 0x10001 for public|constructor and written on 6 bytes -> 818004 ?
        probably we will need to hardcode it as BytesArray
        '''
        Member.__init__(self, parent)
        self.codeOff = ULeb128(self)

        self._data.append(self.codeOff)


class DirectMethod(Method):
    def __init__(self, parent):
        Method.__init__(self, parent)


class VirtualMethod(Method):
    def __init__(self, parent):
        Method.__init__(self, parent)