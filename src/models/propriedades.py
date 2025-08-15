from typing import Optional


class Propriedade:
    def __init__(self, nome: str, custo: int, aluguel: int,
                 proprietario: Optional[str] = None):
        self.nome = nome
        self.custo = custo
        self.aluguel = aluguel
        self.proprietario = proprietario
