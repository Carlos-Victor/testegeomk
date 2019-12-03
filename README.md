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
        - ./source:/source
      ports:
        - 8162:8080
```  
### Pré Requisitos
+ [Docker](https://docs.docker.com/) 17.09.1+
+ [Docker Compose](https://docs.docker.com/compose/) 1.17.0+

### Comandos da aplicação
- Primeiro comando:
```
docker-compose up -d
``` 
- Segundo comando:
```
docker-compose run --rm api python manage.py migrate
```

### Desenvolvido com
+ [Django](https://docs.djangoproject.com/en/3.0/) - Framework Django
+ [Django Rest Framework](https://www.django-rest-framework.org/) - Django Rest Framework
### Desenvolvido por
+ **Carlos Victor** 
