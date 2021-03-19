from enum import Enum

class ResultadosDueloPokemon(Enum):
    POKEMON1 = 0
    POKEMON2 = 1
    EMPATE = 3


class RegaraDoJogo:

    pontuacaoJogador1 = 0
    pontuacaoJogador2 = 0

    def quemGanhaDueloPokemon(self, pokemon1, pokemon2):
        if(pokemon1.getPoder() > pokemon2.getPoder()):
            return ResultadosDueloPokemon.POKEMON1
        elif(pokemon2.getPoder() > pokemon1.getPoder()):
            return ResultadosDueloPokemon.POKEMON2
        else:
            return ResultadosDueloPokemon.EMPATE

    def Lutar(self, jogador1, jogador2):
        pokemonsDoJogador1 = jogador1.getArrayPokemons()
        pokemonsDoJogador2 = jogador2.getArrayPokemons()

        for i in range(3):
            pokemon1 = pokemonsDoJogador1[i]
            pokemon2 = pokemonsDoJogador2[i]

            resultadoDuelo = self.quemGanhaDueloPokemon(
                pokemon1,
                pokemon2
            )

            if(resultadoDuelo == ResultadosDueloPokemon.POKEMON1):
                print(" %s de %s ganhou de %s" %
                      (pokemon1.getNome(), jogador1.getNome(), pokemon2.getNome()))
                self.pontuacaoJogador1 += 1

            elif(resultadoDuelo == ResultadosDueloPokemon.POKEMON2):
                print(" %s de %s ganhou de %s" %
                      (pokemon2.getNome(), jogador2.getNome(), pokemon1.getNome()))
                self.pontuacaoJogador2 += 1

            else:
                print(" %s e %s empataram" %
                      (pokemon1.getNome(), pokemon2.getNome()))

        if(self.pontuacaoJogador1 > self.pontuacaoJogador2):
            print("%s venceu" % (jogador1.getNome()))

        elif(self.pontuacaoJogador2 > self.pontuacaoJogador1):
            print("%s venceu" % (jogador2.getNome()))

        else:
            print("empate")
