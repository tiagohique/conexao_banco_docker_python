# Exemplo de docker Mysql e Python se conectando

Breve descrição do projeto

## Como executar

Apenas rode o seguinte comando no terminal para criar um contêiner Docker com o MySQL:

```bash
docker run -d --name meu-mysql -e MYSQL_ROOT_PASSWORD=sua_senha_aqui -p 3306:3306 mysql:latest
