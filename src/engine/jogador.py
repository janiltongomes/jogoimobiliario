import random


class Jogador:
    def __init__(self, nome: str):
        self.nome = nome
        self.saldo = 0
        self.posicao = 0
        self.propriedades = []

    def esta_ativo(self) -> bool:
        return self.saldo >= 0

    def comprar(self, propriedade) -> bool:
        if self.saldo >= propriedade.custo:
            self.saldo -= propriedade.custo
            self.propriedades.append(propriedade)
            propriedade.proprietario = self
            return True
        return False


class Impulsivo(Jogador):
    def decidir_compra(self, propriedade) -> bool:
        return True


class Exigente(Jogador):
    def decidir_compra(self, propriedade) -> bool:
        return propriedade.aluguel > 50


class Cauteloso(Jogador):
    def decidir_compra(self, propriedade) -> bool:
        return self.saldo - propriedade.custo >= 80


class Aleatorio(Jogador):
    def decidir_compra(self, propriedade) -> bool:
        return random.choice([True, False])
