from GrammarVisitor import GrammarVisitor
from GrammarParser import GrammarParser

class MyVisitor(GrammarVisitor):
    def __init__(self):
        self.memory = {}
        
    # definimos la accion de asiganacion 
    def visitAssign(self,ctx):
        # Se obtiene el id o nombre de la variables 
        name=ctx.ID().getText()
        # Se obtiene el valor de la expresion o numerico
        value=self.visit(ctx.expr())
        # Se alamacena en memoria partir del nombre y valor 
        self.memory[name]=value
        
    # Definimos la accion de impresion 
    def visitPrint(self,ctx):
        # Definimos la expresion del valor que se desea mostrar 
       value=self.visit(ctx.expr())   
       # imprime el valor 
       print(value)  
       
       # Definimos las expresiones 
       def visitExpr(selg,ctx):
           # Busca si existe ID 
           if ctx.ID():
               # Obtiene del contexto el nombre de la variable 
               name=ctx.ID().getText()
               # Si el nombre de la variable no est, lanza un error
               if name not in self.memory:
                   raise NameError(f"Variable'{name}'no definida")
               #Si existe retorna el valor de la variable 
               return self.memory[name]
           # Busca el operador 
           elif ctx.op:
               # visita y obtiene el lado izquierdo 
               left=self.visit(ctx.expr(0))
               # Visita y obtiene lado derecho 
               right=self.visit(ctx.expr(1))
               # Evalua la operacion 
               if ctx.op.text=='+':
                   return left+right
               if ctx.op.text=='-':
                   return left-right
               if ctx.op.text=='*':
                   return left*right
               if ctx.op.text=='/':
                   # verifica la division por cero 
                   if right==0:
                       raise ValueError("Division por cero")
                   return left/right
               
       
       