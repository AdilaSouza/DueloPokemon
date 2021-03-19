
class Treinador:
    nome = None
    idade = None
    pokemonArray = []

    def __init__(self, nome=None, idade=None, pokemonArray=[]):
        self.nome = nome
        self.idade = idade
        self.pokemonArray = pokemonArray
    
    def getArrayPokemons(self):
        return self.pokemonArray
    
    def getNome(self):
        return self.nome

    def mostrar(self):
        resultado = "\n"
        resultado += "nome: %s\n" %self.nome
        resultado += "idade: %s\n" %self.idade
        resultado += "pokemons: %s\n" %self.mostrarPokemons()
        print(resultado)
    
    def mostrarPokemons(self):
        resultado = "\n"
        for pokemon in self.pokemonArray:
            resultado += pokemon.mostrar()
        return resultado
