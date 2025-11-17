# Sistema de Login com Flask

## Descrição

Este projeto é uma aplicação web desenvolvida com Flask que implementa um sistema de autenticação de usuários. Ele permite o cadastro, login, logout e controle de acesso a páginas protegidas. O sistema utiliza SQLite como banco de dados e SQLAlchemy como ORM, além do Flask-Login para gerenciamento de sessões.

## Funcionalidades

- Cadastro de novos usuários
- Login de usuários existentes
- Logout
- Proteção de rotas (acesso restrito a usuários autenticados)
- Armazenamento seguro de dados no banco SQLite

## Estrutura do Projeto

```
Sistema_login_flask/
│
├── main.py                # Arquivo principal da aplicação Flask
├── db/
│   ├── db.py              # Configuração do banco de dados SQLAlchemy
│   └── __init__.py
├── models/
│   ├── models.py          # Definição do modelo de usuário
│   └── __init__.py
├── routes/
│   ├── user_route.py      # Rotas de autenticação e usuário
│   └── __init__.py
├── static/
│   └── style.css          # Arquivo de estilos CSS
├── templates/
│   ├── base.html          # Template base
│   ├── home.html          # Página inicial (protegida)
│   ├── login.html         # Página de login
│   └── register.html      # Página de cadastro
├── README.md              # Documentação do projeto
└── LICENSE                # Licença de uso
```

## Instalação

1. **Clone o repositório:**
   ```powershell
   git clone https://github.com/FelipeHoffmannV/Sistema_login_flask.git
   ```

2. **Crie e ative um ambiente virtual:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   pip install flask flask_sqlalchemy flask_login
   ```

4. **Execute a aplicação:**
   ```powershell
   python main.py
   ```

## Uso

- Acesse `http://localhost:5000` no navegador.
- Cadastre um novo usuário na página de registro.
- Faça login para acessar a página protegida.
- Use o botão de logout para encerrar a sessão.

## Modelos

### Usuário

- `id`: Identificador único
- `nome`: Nome de usuário (único)
- `senha`: Senha do usuário

## Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite

## Licença

Este projeto está sob a licença MIT.

