from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}
        
    # definimos la accion de asiganacion 
    def visitAssign(self,ctx):
        name=ctx.ID().getText()
        value=self.visit(ctx.expr())
        self.memory[name]=value
        
    # Definimos la accion de impresion 
    def visitPrint(self,ctx):
       value=self.visit(ctx.expr())   
       print(value)  
       
       