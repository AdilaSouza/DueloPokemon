from pokemon import Pokemon
from treinador import Treinador
from regrasDoJogo import RegaraDoJogo

def main():
    pikashu = Pokemon(nome="Pikashu", poder=400, tipo="elétrico")
    charmander = Pokemon(nome="Charmander", poder=300, tipo="fogo")
    snorlax = Pokemon(nome="Snorlax", poder=100, tipo="normal")

    arrayDePokemonsAsh = [pikashu, charmander, snorlax]
    arrayDePokemonsMisty = [pikashu, snorlax, snorlax]

    ash = Treinador(nome="Ash catchup", idade=20, pokemonArray=arrayDePokemonsAsh)
    misty = Treinador(nome="Misty", idade=23, pokemonArray=arrayDePokemonsMisty)

    RegaraDoJogo().Lutar(ash, misty)

if __name__ == "__main__":
    main()
    
