#  API para Estacionamento (v0.1)

API para Estacionamento
### Sumário
+ [Iniciando](#iniciando-com-docker-compose)
+ [Pré Requisitos](#pré-requisitos)
+ [Comandos da aplicação](#comandos-da-aplicação)
+ [Desenvolvido com](#desenvolvido-com)
+ [Versionamento](#versionamento)
+ [Desenvolvido por](#desenvolvido-por)
 
### Iniciando com Docker Compose
+ Exemplo:

```yaml
version: '3'
services:
    api:
      build:
        context: .
        dockerfile: ./dockers/Dockerfile
      container_name: api_teste
      command: python manage.py runserver 0.0.0.0:8080
      env_file:
        - ./env/api.env
      volumes:
        - ./source:source
      ports:
        - 8162:8080
```  
### Pré Requisitos
+ [Docker](https://docs.docker.com/) 17.09.1+
+ [Docker Compose](https://docs.docker.com/compose/) 1.17.0+

### Comandos da aplicação
```
python manage.py test nome_app.tests.arquivo_teste
```  

### Desenvolvido com
+ [Django](https://angular.io/docs) - Framework Django
+ [Django Rest Framework](https://angular.io/docs) - Django Rest Framework
### Desenvolvido por
+ **Carlos Victor** 