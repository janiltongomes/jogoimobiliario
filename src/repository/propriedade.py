from engine.propriedade import Propriedade


class PropriedadeRepository:
    """Repositorio Propriedade."""

    def __init__(self, db_connection):
        self.db = db_connection

    def listar_todas(self):
        """listar propriedades."""
        query = "SELECT nome, custo, aluguel FROM propriedades"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            resultados = cursor.fetchall()

        propriedades = []
        for row in resultados:
            nome, custo, aluguel = row
            prop = Propriedade(nome=nome, custo=custo, aluguel=aluguel)
            prop.proprietario = None
            propriedades.append(prop)

        return propriedades
