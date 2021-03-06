import sys

from Cparser import Cparser
from Interpreter import Interpreter
from TreePrinter import TreePrinter
from TypeChecker_2 import TypeChecker
import ply.yacc as yacc


if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

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
