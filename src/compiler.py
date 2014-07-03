from ply import yacc
import sys

from Cparser import Cparser
from Interpreter import Interpreter
from TreePrinter import TreePrinter
from TypeChecker_2 import TypeChecker
from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.items.header_item import HeaderItem
from src.items.string_data_item import StringDataItem
from src.items.string_id_item import StringIdItem
from src.parser.dex import Dex
from src.sections.string_data_item_section import StringDataItemSection


if __name__ == '__main__':

    header = HeaderItem(None)
    print header.getIndexOffset(3)
    print header.getBytesCount()
    print header.getGlobalOffset()

    header.signature._data.append(Bytes(None, 1))

    print header.getIndexOffset(5)
    print header.getBytesCount()

    print header.data_off.value
    print header.data_off.bytesCount
    print header.data_off.data

    header.data_off.bytesCount = 8

    print header.data_off.value
    print header.data_off.bytesCount
    print header.data_off.data

    print header.data_off.value
    print header.data_off.bytesCount
    print header.data_off.data

    stringId = StringIdItem(None)
    print
    print stringId.getBytesCount()
    print stringId.getIndexOffset(1)

    stringDataItem = StringDataItem(None)
    print 'stringDataItem:'

    string = "abcd123"
    stringDataItem.setString(string)

    print stringDataItem.utf16Size
    print stringDataItem.string
    for x in stringDataItem.string._data:
        print x.value
        print x.data

    #debug data above

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    output = open("../test.txt", "wb")

    dex = Dex()
    #dex.printItem(output)

    print "CParsing:"
    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    ast = parser.parse(text, lexer=Cparser.scanner)
    if ast is None:
        sys.exit(-1)

    interpreter = Interpreter(dex)
    
    try:
        ast.printTree(0)
        semantic_errors_found = TypeChecker().dispatch(ast)
        if not semantic_errors_found:
            ast.accept(interpreter)
    except Exception:
        print "Error while printing tree or performing type-check caused by previous syntax errors."
        
    #interpreter.dex.printItem(output)
