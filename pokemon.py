
class Pokemon:
    nome = None
    tipo = None
    poder = None

    def __init__(self, nome=None, tipo=None, poder=None):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder
    
    def getNome(self):
        return self.nome

    def getPoder(self):
        return self.poder

    def mostrar(self):
        resultado = "\n"
        resultado += "nome: %s\n" %self.nome
        resultado += "tipo: %s\n" %self.tipo
        resultado += "poder: %d\n" %self.poder
        return resultado
