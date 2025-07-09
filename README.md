# 📝 do.it | Lista de Tarefas

**do.it** é uma aplicação simples e intuitiva para organização de tarefas, desenvolvida com foco em uma interface clara e funcional. O projeto foi criado para fins educacionais e práticos de desenvolvimento full stack, incluindo backend em Django.

## 🔗 Sobre o projeto

A ideia central do **do.it** é permitir ao usuário criar listas de tarefas de forma rápida e eficaz, com uma interface amigável, responsiva e segura. O projeto é ideal para quem está começando a estudar desenvolvimento web full stack e deseja entender na prática como estruturar uma aplicação com frontend em HTML, CSS, JavaScript (JSX e jQuery) e backend com Django.

## 🧩 Funcionalidades atuais

- Criação de listas de tarefas com autenticação de usuário
- Inserção dinâmica de itens com formulários e validação
- Marcar tarefas como concluídas via checkbox
- Remoção individual de tarefas
- Interface responsiva e estilizada
- Mensagens de erro e feedback em formulários (login e registro)
- Botões para manipulação da interface

## ⚙️ Tecnologias utilizadas

### Frontend
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/HTML) 
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/pt-BR/docs/Web/CSS)  [![JavaScript (JSX)](https://img.shields.io/badge/JSX-61DAFB?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)  [![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)

### Backend
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  [![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

## 🛠 Estrutura do projeto

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


## 🚧 Melhorias previstas

Este projeto pode ser expandido com:

- Armazenamento e sincronização de tarefas no banco de dados via Django ORM
- Perfis e gerenciamento avançado de usuários
- Animações e melhorias de usabilidade no frontend
- Refatoração do código JSX e templates para maior modularidade
- Testes automatizados (unitários e funcionais)

## 👨‍💻 Autor

Desenvolvido por [Itamar Medeiros](https://github.com/ItamarMedeirosDev) como parte de sua jornada de aprendizado em desenvolvimento web full stack.

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://itamarmedeirosdev.vercel.app/) 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/itamarmedeiros6/)

## 🌐 Deploy

A aplicação está hospedada em produção na plataforma [Railway](https://railway.app), utilizando:

- **Servidor:** Gunicorn com Whitenoise
- **Banco de Dados:** PostgreSQL
- **Gerenciamento de variáveis de ambiente:** Railway Dashboard
- **Coleta de arquivos estáticos:** `collectstatic` com armazenamento via `staticfiles/`

🔗 Acesse a versão em produção: [https://doitnow.up.railway.app](https://doitnow.up.railway.app)


## Colaboração

Este projeto contou com a colaboração de Victor Rodrigues ([@victormelkor](https://github.com/victormelkor)).

[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=google-chrome&logoColor=white)](https://victormelkor.github.io) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/victormelkor/)



