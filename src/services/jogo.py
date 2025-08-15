from engine.jogo import Jogo
from engine.jogador import Impulsivo, Exigente, Cauteloso, Aleatorio
from repository.propriedade import PropriedadeRepository
from repository.config import ConfigRepository
import random


class JogoService:
    def __init__(self, db):
        self.prop_repo = PropriedadeRepository(db)
        self.config_repo = ConfigRepository(db)
        self.config = self.config_repo.listar_todas()

    def simular(self):
        # busca propriedades do DB
        propriedades = self.prop_repo.listar_todas()
        for p in propriedades:
            p.proprietario = None

        # cria jogadores
        jogadores = [
            Impulsivo("impulsivo"),
            Exigente("exigente"),
            Cauteloso("cauteloso"),
            Aleatorio("aleatorio"),
        ]
        random.shuffle(jogadores)

        # cria jogo passando configs do banco
        jogo = Jogo(
            jogadores=jogadores,
            propriedades=propriedades,
            saldo_inicial=self.config.get("SALDO_INICIAL", 300),
            bonus_voltar=self.config.get("BONUS_VOLTAR_TABULEIRO", 100),
            max_rodadas=self.config.get("MAX_RODADAS", 1000)
        )

        vencedor, ranking = jogo.rodar()
        return {"vencedor": vencedor, "jogadores": ranking}
