'''
Created on Nov 15, 2016

@author: Carolina
'''



class MaqCalculadora:
    def __init__(self):
        self.memoria=0
        self.memres=0
        
    def incrementa_soma(self,valor):
        self.memoria+=valor
    
    def incrementa_sub(self,valor):
        self.memoria-=valor
    
    def soma(self,op1,op2):
        if op2==0:
            resultado=self.memres+op1
        else:
            resultado=op1+op2
        self.memres=resultado
        return resultado
                   
    def getMemoria(self):
        return self.memoria
    