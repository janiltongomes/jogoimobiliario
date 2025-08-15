# Jogo Imobiliário API
> API simples que simula um jogo imobiliario. Toda vez que a url principal for chamada, será executado a simulação do jogo retornando um json com o vencedor e os participantes ( http://localhost:8000/jogo/simular ).
> Os Imóveis ( propriedades ) estão sendo inicializadas e configuradas no banco de dados. Para simulações diferentes, deverá ser ajustado os valores no banco.

## Dependências

- Python 3.13
- PostgreSQL
- Docker e Docker Compose

## Passos para desenvolvimento (com Docker)

1. Clone o repositório:

```bash
git clone https://github.com/seunome/jogo-imobiliario.git
cd jogo-imobiliario
```


2. Crie um arquivo .env baseado no modelo .env.example e configure as variáveis de ambiente
3. Inicialize o banco de dados com Docker Compose (os seeds serão carregados automaticamente se o banco estiver vazio)

```sh
docker-compose up -d db
```

4. Construa e execute a aplicação via Docker:

```sh
docker-compose up --build app
```



A API estará disponível em:

http://localhost:8000/jogo/simular