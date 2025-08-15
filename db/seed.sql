CREATE TABLE IF NOT EXISTS propriedades (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    custo INT NOT NULL,
    aluguel INT NOT NULL,
    proprietario VARCHAR(50)
);

INSERT INTO propriedades (nome, custo, aluguel, proprietario) VALUES
('A1', 60, 10, NULL),
('A2', 60, 10, NULL),
('B1', 100, 20, NULL),
('B2', 100, 20, NULL),
('C1', 120, 30, NULL),
('C2', 120, 30, NULL),
('D1', 140, 35, NULL),
('D2', 140, 35, NULL),
('E1', 160, 40, NULL),
('E2', 160, 40, NULL),
('F1', 180, 50, NULL),
('F2', 180, 50, NULL),
('G1', 200, 55, NULL),
('G2', 200, 55, NULL),
('H1', 220, 60, NULL),
('H2', 220, 60, NULL),
('I1', 240, 70, NULL),
('I2', 240, 70, NULL),
('J1', 260, 80, NULL),
('J2', 260, 80, NULL);

CREATE TABLE jogo_config (
    chave VARCHAR PRIMARY KEY,
    valor VARCHAR NOT NULL
);

INSERT INTO jogo_config (chave, valor) VALUES
('SALDO_INICIAL', '300'),
('BONUS_VOLTAR_TABULEIRO', '100'),
('MAX_RODADAS', '1000'),
('NUM_PROPRIEDADES', '20');