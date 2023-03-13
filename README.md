# Docker

## Sobre
Este projeto é composto por uma aplicação flask com seis endpoints que realizam o CRUD num banco de dados MYSQL. A intenção é exercitar os conhecimentos de docker e docker-compose.

## Endpoints
* [GET] "/": verifica se a aplicação está funcionando e se é possível realizar requisições para a API
* [POST] "/insert": insere usuário no banco de dados. 
* [GET] "/read": consulta usuário registrado no banco de dados por nome
* [PUT] "/update": atualiza dados de usuário por nome
* [DELETE] "/delete": remove usuário do banco de dados por nome
* [GET] "/all_users": apresenta todos os usuários registrados no banco de dados

## Como executar
Para executar subir a aplicação e o banco é necessário apenas executar o comando:
``` 
docker-compose -f docker-compose.yml up 
```
Após isso, os endpoints podem ser acessados acessando o localhost na porta 3000. Para isso, utilizei a ferramenta `Postman`.
