# Jogo Imobiliário API
> API simples que simula um jogo imobiliario. Toda vez que a url principal for chamada, será executado a simulação do jogo retornando um json com o vencedor e os participantes ( http://localhost:8000/jogo/simular ).
> Os Imóveis ( propriedades ) estão sendo inicializadas e configuradas no banco de dados. Para simulações diferentes, deverá ser ajustado os valores no banco.
> O projeto usa as portas 8080 e 5432 como padrão. Verifique se as portas estão sendo usadas antes de executar o projeto.

## Dependências

- Python 3.13
- PostgreSQL
- Docker e Docker Compose

## Passos para desenvolvimento (com Docker)

1. Clone o repositório:

```bash
git clone https://github.com/janiltongomes/jogoimobiliario.git
```
```bash
cd jogoimobiliario
```

2. Crie um arquivo .env baseado no modelo .env.example e configure as variáveis de ambiente

3. Inicialize o banco de dados com Docker Compose (os seeds serão carregados automaticamente se o banco estiver vazio)

```sh
docker-compose up -d db
```

4. Construa e execute a aplicação via Docker:

```sh
docker-compose up -d app
```



A API estará disponível em:

http://localhost:8080/jogo/simular