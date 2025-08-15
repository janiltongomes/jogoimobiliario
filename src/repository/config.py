class ConfigRepository:
    def __init__(self, db_connection):
        self.db = db_connection

    def listar_todas(self):
        query = "SELECT chave, valor FROM jogo_config"
        with self.db.cursor() as cursor:
            cursor.execute(query)
            resultados = cursor.fetchall()

        config = {}
        for chave, valor in resultados:
            try:
                config[chave] = int(valor)
            except ValueError:
                config[chave] = valor
        return config
