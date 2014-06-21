from src.items.bytes import Bytes
from src.parser.measurable import Measurable


class DebugInfoItem(Measurable):
    '''
    classdocs
    '''

    def __init__(self, parent):
        '''
        Constructor
        '''
        Measurable.__init__(self, parent)

        self.line_start = Bytes(self, 4)
        self.parameters_size = Bytes(self, 4)
        self.debugOpcodes = []

        self._data = [self.line_start, self.parameters_size, self.debugOpcodes]


class DebugOpcode(Measurable):
    def __init__(self, parent):
        Measurable.__init__(self, parent)
        self.address_diff = Bytes(self, 4)
        self.line_diff = Bytes(self, 4)

        self._data = [self.address_diff, self.line_diff]