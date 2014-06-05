'''
Created on 5 cze 2014

@author: Przemek
'''
from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class ClassDataItem(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        self.staticFieldsSize = Bytes(self, 1)
        self.instanceFieldsSize = Bytes(self, 1)
        self.directMethodsSize = Bytes(self, 1)
        self.virtualMethodsSize = Bytes(self, 1)
        self.staticFields = []
        self.instanceFields = []
        self.directMethods = []
        self.virtualMethods = []
        
        self._data = [self.staticFieldsSize, self.instanceFieldsSize, self.directMethodsSize, self.virtualMethodsSize, 
                      self.staticFields, self.instanceFields, self.directMethods, self.virtualMethods]
    
class Member(Measurable):    

    def __init__(self, parent):
        Measurable.__init__(self, parent)
        self.fieldIdxDiff = Bytes(self, 1)
        self.accessFlags = Bytes(self, 1)
        
        self._data = [self.fieldIdxDiff, self.accessFlags]
        
class StaticField(Member):
    
    def __init__(self, parent):
        Member.__init__(self, parent)
        #didn't see one, need to check maybe
        
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
        self.codeOff = Bytes(self, 2)  
        
        self._data.append(self.codeOff)      
        
class DirectMethod(Method):
    
    def __init__(self, parent):
        Method.__init__(self, parent)
        
class VirtualMethod(Method):
    
    def __init__(self, parent):
        Method.__init__(self, parent)