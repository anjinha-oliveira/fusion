# Projeto Fusion
## Construindo uma Aplicação Web com Django

Projeto desenvolvido para aprender sobre a construção de uma aplicação web utilizando o framework Django.</br>
Para isso, utilizei um template da web e fui desenvolvendo a aplicação a partir de cada seção do mesmo.

### Instruções de Instalação

1. Clone o repositório:

   ```sh
   $ git clone https://github.com/anjinha-oliveira/fusion.git
   $ cd fusion
   ```

### Crie e ative um ambiente virtual

```sh
$ python3 -m virtualenv .venv
$ source .venv/bin/activate
```

### Instale as dependências

```sh
$ pip install -r requirements.txt
```

### Execute as migrações do Django:

```sh
$ python manage.py migrate
```

### Executando a aplicação (Execute comando no root do projeto)

```sh
$ python manage.py runserver 8080
```

A aplicação estará disponível em http://localhost:8080/

### Tecnologias Utilizadas

* Python (Versão 3.12)
* Django (Versão 5.0.2)
* Dj-Database-URL
* Python-Decouple
* Django-StdImage
* uWSGI
* Dj-Static

### Deploy Vercel

A aplicação está disponível em https://fusion-phi.vercel.app/