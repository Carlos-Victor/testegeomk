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
  aj100f:
    image: registry.geomk.com.br/aj100f:v1.0.5
    restart: unless-stopped
    ports:
    - '80:80'
    environment:
    - NGINX_PORT=80
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