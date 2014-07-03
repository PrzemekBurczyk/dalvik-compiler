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

    def append(self, code_item):
        self.data.insert(len(self.data) - 1, code_item)

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.data.append(Bytes(self, 2))
        
        code_item = CodeItem(self)
        code_item.registersSize.value = 1
        code_item.insSize.value = 1
        code_item.outsSize.value = 1
        code_item.triesSize.value = 0
        code_item.insnsSize.value = 4
        
        instruction = Instruction(code_item)
        byte = Bytes(instruction, 2)
        byte.value = 0x1070
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(code_item)
        byte = Bytes(instruction, 2)
        byte.value = 2
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(code_item)
        byte = Bytes(instruction, 2)
        byte.value = 0
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        instruction = Instruction(code_item)
        byte = Bytes(instruction, 2)
        byte.value = 0xe
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        self.append(code_item)
        
        code_item = CodeItem(self)
        code_item.registersSize.value = 1
        code_item.insSize.value = 1
        code_item.outsSize.value = 0
        code_item.triesSize.value = 0
        code_item.insnsSize.value = 1
        
        instruction = Instruction(code_item)
        byte = Bytes(instruction, 2)
        byte.value = 0xe
        instruction.data.data.append(byte)
        
        code_item.instructions.append(instruction)
        
        self.append(code_item)