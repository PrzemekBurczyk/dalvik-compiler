import sys

from ply import yacc

from Cparser import Cparser
from TreePrinter import TreePrinter
from Interpreter import Interpreter
from TypeChecker_2 import TypeChecker
from src.items.bytes import Bytes
from src.items.bytes_array import BytesArray
from src.items.header_item import HeaderItem
from src.items.string_data_item import StringDataItem
from src.items.string_id_item import StringIdItem
from src.parser.dex import Dex
from src.sections.string_data_item_section import StringDataItemSection


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    output = open("../test.txt", "wb")

    dex = Dex()

    dex.printItem(output)

    print "CParsing:"
    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    ast = parser.parse(text, lexer=Cparser.scanner)
    if ast is None:
        sys.exit(-1)

    try:
        ast.printTree(0)
        semantic_errors_found = TypeChecker().dispatch(ast)
        if not semantic_errors_found:
            ast.accept(Interpreter())
    except Exception:
        print "Error while printing tree or performing type-check caused by previous syntax errors."
