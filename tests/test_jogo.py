from repository.db import get_connection
from services.jogo import JogoService


def test_simular_jogo():
    conn = get_connection()
    service = JogoService(conn)
    resultado = service.simular()
    conn.close()

    # Verifica as chaves
    assert "vencedor" in resultado
    assert "jogadores" in resultado
    assert isinstance(resultado["jogadores"], list)
    assert len(resultado["jogadores"]) == 4

    assert resultado["vencedor"] in resultado["jogadores"]
