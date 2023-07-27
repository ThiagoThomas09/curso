# Eventex

Sistema de Eventos encomendado pelo Fulano.

## Como desenvolver?

1. Clone o repositorio.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env
6. Execute os testes.

```console
git clone git@github.com:ThiagoThomas09/curso.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instancia no pythonanywhere.
2. Envia as configuracoes para o pythonanywhere
3. Define uma SECRET_KEY segura para a instancia
4. Defina DEBUG=False
5. Configure o servico de email.
6. Envie o codigo para o pythonanywhere

```console
Configuracoes para o pythonanywhere...
```