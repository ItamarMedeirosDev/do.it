# Documentação do Projeto do.it

Bem-vindo à documentação oficial do projeto **do.it** — um gerenciador de tarefas minimalista desenvolvido com Django.

---

## 🔖 Índice

- [Visão Geral](#visão-geral)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Apps Django](#apps-django)
- [Comandos Úteis](#comandos-úteis)
- [Licença](#licença)

---

## Visão Geral

O **do.it** é uma aplicação web com autenticação de usuários e gerenciamento de tarefas, focada em simplicidade e experiência do usuário.

---

## Requisitos

- Python 3.11+
- Django 5.2.x
- SQLite (ou outro banco configurado)
- Node.js (se for usar build de assets com ferramentas JS)
- Ambiente virtual Python (recomendado)

---

## Instalação

```bash
git clone https://github.com/seu-usuario/doit.git
cd doit
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate no Windows
pip install -r requirements.txt
cp .env.example .env  # e edite com seus dados reais
python manage.py migrate
python manage.py runserver
```


## Estrutura do Projeto
```
📁 do.it
├── manage.py # Script de gerenciamento do Django
├── backend/ # Configurações Django
├── tasks/ # App de tarefas (models, views, templates)
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ └── forms.py
├── users/ # App de gestão de usuários (models, views, forms, etc)
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ └── forms.py
├── static/
│ ├── style.css # Estilos principais
│ └── script.jsx # Lógica frontend
├── README.md
├── DOCUMENTATION.md
├── index.html
├── task_list.html
├── login.html
└── register.html
```

## Variáveis de Ambiente

```
.env.example
SECRET_KEY=chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

Use `python-decouple`, `django-environ` ou `os.getenv()` para lidar com elas no `settings.py`.

## Apps Django
`users/`
- Registro com CustomUser usando email
- Login, logout e validação de senha
- Formulários personalizados (CustomUserCreationForm)

`tasks/`
- CRUD de tarefas (adicionar, concluir, apagar)
- Tarefas vinculadas ao usuário autenticado
- Views protegidas com @login_required

## Comandos Úteis

```
pip install -r requirements.txt
python manage.py createsuperuser
python manage.py collectstatic
python manage.py check --deploy
```

## Licença
Este projeto está sob a licença MIT. Veja LICENSE para detalhes.