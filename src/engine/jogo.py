import random


class Jogo:
    def __init__(self, jogadores, propriedades, saldo_inicial,
                 bonus_voltar, max_rodadas):
        self.jogadores = jogadores
        self.propriedades = propriedades
        self.saldo_inicial = saldo_inicial
        self.bonus_voltar = bonus_voltar
        self.max_rodadas = max_rodadas
        self.rodada = 0

        # inicializa saldo dos jogadores
        for j in self.jogadores:
            j.saldo = self.saldo_inicial

    def rolar_dado(self) -> int:
        return random.randint(1, 6)

    def mover_jogador(self, jogador):
        dado = self.rolar_dado()
        old_pos = jogador.posicao
        jogador.posicao = (jogador.posicao + dado) % len(self.propriedades)

        if old_pos + dado >= len(self.propriedades):
            jogador.saldo += self.bonus_voltar
        return jogador.posicao

    def jogar_turno(self, jogador):
        if not jogador.esta_ativo():
            return

        pos = self.mover_jogador(jogador)
        propriedade = self.propriedades[pos]

        if propriedade.proprietario is None:
            if jogador.decidir_compra(propriedade):
                jogador.comprar(propriedade)
        elif propriedade.proprietario != jogador:
            jogador.saldo -= propriedade.aluguel
            propriedade.proprietario.saldo += propriedade.aluguel
            if jogador.saldo < 0:
                for p in jogador.propriedades:
                    p.proprietario = None
                jogador.propriedades = []

    def rodar(self):
        while self.rodada < self.max_rodadas:
            self.rodada += 1
            for jogador in self.jogadores:
                self.jogar_turno(jogador)
                ativos = [j for j in self.jogadores if j.esta_ativo()]
                if len(ativos) == 1:
                    return ativos[0].nome, [j.nome for j in sorted(self.jogadores, key=lambda x: x.saldo, reverse=True)]

        # desempate pelo saldo caso exceda max_rodadas
        ranking = sorted(self.jogadores, key=lambda x: x.saldo, reverse=True)
        return ranking[0].nome, [j.nome for j in ranking]
