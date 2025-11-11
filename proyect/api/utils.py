from antlr4 import * 
from lenguage.GrammarLexer import GrammarLexer
from lenguage.GrammarParser import GrammarParser
import lenguage.MyVisitor as MyVisitor
import sys
import io

# Metodo que no permite ejecutra el codigo 
def run_code(code:str):
    input_stream=InputStream(code)
    lexer=GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()
    
    # Captura las salidas 
    old_stdout=sys.stdout()
    buf=io.StringIO()
    sys.stdout=buf
    #Creamos un objeto de nuestro visitor 
    visitor=MyVisitor()
    #Vsitamos el arbol con nuestro visitor
    visitor.visit(tree)
    # Capturamos un objeto de nuestro visitor 
    output=buf.getvalue()
    
    return output 
