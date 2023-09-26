# Sobre

Este é um protótipo de rede social feito para a disciplina de Software Product do Curso de Análise e Desenvolvimento de Software da Faculdade Impacta.

# Features

- Registro de usuários
- Login e logout de usuários
- Postagem de mensagens públicas no perfil de outros usuários
- Deleção de mensagens

# Requisitos

Para rodar o projeto, é necessário ter Python 3.8 ou superior instalado em ambiente local

# Rodando o projeto localmente

Criar Virtualenv:

```shell
python3 -m venv venv
```

Ativar Virtualenv:

```shell
source venv/bin/activate
```

Instalar dependências:

```shell
pip install -r requirements.txt
```

Rodar migrações:

```shell
python3 src/manage.py migrate
```

Rodar servidor

```shell
python3 src/manage.py runserver
```

A aplicação poderá ser acessada via localhost em `127.0.0.1:8000`