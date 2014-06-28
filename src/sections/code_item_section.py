'''
Created on 5 cze 2014

@author: Przemek
'''
from src.parser.measurable import Measurable
from src.items.code_item import CodeItem, Instruction
from src.items.bytes import Bytes


class CodeItemSection(Measurable):
    '''
    classdocs
    '''


    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)
        
        code_item = CodeItem(self)
        code_item.registersSize.value = 1
        code_item.insnsSize.value = 1
        code_item.outsSize.value = 1
        code_item.triesSize.value = 1
        code_item.insnsSize.value = 4
        
        instruction = Instruction(self)
        byte = Bytes(self, 2)
        byte.value = 701
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(self)
        byte = Bytes(self, 2)
        byte.value = 2
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(self)
        byte = Bytes(self, 2)
        byte.value = 0
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(self)
        byte = Bytes(self, 2)
        byte.value = 1 # to fix
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        self.data.append(code_item)
        
        code_item = CodeItem(self)
        code_item.registersSize.value = 1
        code_item.insnsSize.value = 1
        code_item.outsSize.value = 0
        code_item.triesSize.value = 0
        code_item.insnsSize.value = 1
        
        instruction = Instruction(self)
        byte = Bytes(self, 2)
        byte.value = 1 # to fix
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        self.data.append(code_item)
        
        