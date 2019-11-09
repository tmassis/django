# Eventex 

Sistema de Eventos encomendado pela Morena

[![Build Status](https://travis-ci.org/PaulaFAlves/eventex.svg?branch=master)](https://travis-ci.org/PaulaFAlves/eventex)

[![codecov](https://codecov.io/gh/PaulaFAlves/eventex/branch/master/graph/badge.svg)](https://codecov.io/gh/PaulaFAlves/eventex)

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com .env.
6. Execute os textes.

```console
git clone git@github.com:tmassis/django.git django
cd django
python -m venv .django
source .django/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no Heroku
2. Envie as configurações para o Heroku
3. Defina uma SECRET_KEY segura para a instância 
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroky config:set DEBUG=False
# configuro o email
git push heroku master --force
```

