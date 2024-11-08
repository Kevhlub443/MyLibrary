# MyLibrary
MyLibrary é um sistema para gerenciar sua coleção de livros. Cadastre, filtre e visualize livros por título, autor, assunto, status e localização. A ferramenta permite controlar facilmente sua biblioteca pessoal, mantendo um registro claro e acessível de todos os livros disponíveis.


![MyLibrary em português](https://github.com/user-attachments/assets/1262695d-18a8-4a10-ad8c-790c89b80bc4)



```markdown
# Livro Organizado - Sistema de Gestão de Livros

Este é um projeto para organizar e gerenciar a coleção de livros de uma casa. O sistema permite cadastrar livros, filtrar por autor,
assunto, status (disponível, emprestado), localização (estante e seção) e acompanhar a disponibilidade de cada livro.

## Tecnologias Utilizadas

- **Backend**:
  - **Python 3.x** com **Django** (para o desenvolvimento da API e gerenciamento do banco de dados)
  - **MySQL** (para o banco de dados)
  - **AJAX** (para requisições assíncronas no front-end)
  
- **Frontend**:
  - **HTML5**, **CSS3** (estruturação e estilização das páginas)
  - **Bootstrap 5** (framework CSS para design responsivo e moderno)
  - **JavaScript** (para interatividade e requisições AJAX)

- **Versionamento**:
  - **Git** (para controle de versão)

## Funcionalidades

- **Cadastro de livros**: Permite adicionar informações sobre os livros, como título, autor, assunto, temas, e localização.
- **Filtro de livros**: Os livros podem ser filtrados por assunto, autor, status (disponível ou emprestado), e localização.
- **Alteração de status**: O status do livro pode ser alterado para "emprestado" ou "disponível".
- **Visualização de detalhes**: Exibe as informações detalhadas de cada livro, como autor, temas, localização, e status.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:


```
##
### 0. O projeto está organizado da seguinte forma:

```markdown
/Mylibrary/                     # Diretório principal do projeto
│
├── /backend/                            # Código do servidor (Django)
│   ├── /livros/                         # Aplicação Django para gerenciar livros
│   │   ├── /migrations/                 # Arquivos de migração do banco de dados
│   │   ├── /templates/                  # Templates HTML do backend (caso precise renderizar views)
│   │   ├── /static/                    # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── admin.py                    # Configuração do painel administrativo
│   │   ├── models.py                   # Modelos de banco de dados (Livro, Usuário, etc)
│   │   ├── views.py                    # Views para lidar com as requisições da API
│   │   ├── serializers.py              # Serialização de dados (converte entre objetos e JSON)
│   │   ├── urls.py                     # URLs da aplicação
│   │   └── forms.py                    # Formulários para cadastrar/editar livros
│   ├── /config/                        # Configurações do Django
│   │   ├── settings.py                 # Configurações principais (banco de dados, instâncias)
│   │   ├── urls.py                     # URLs principais do backend
│   │   └── wsgi.py                     # Entrada para o servidor web
│   ├── manage.py                       # Comando de gerenciamento do Django
│
├── /frontend/                           # Código do cliente (HTML, CSS, JS, Bootstrap)
│   ├── /assets/                        # Arquivos estáticos para o front-end (imagens, fontes)
│   ├── /js/                            # Scripts JavaScript (AJAX para comunicação com a API)
│   ├── /css/                           # Arquivos CSS (estilos da página)
│   ├── index.html                      # Página inicial que exibe os livros
│   ├── cadastro.html                   # Página de cadastro de livro
│   └── detalhes.html                   # Página de detalhes do livro
│
├── /database/                           # Banco de dados (MySQL)
│   ├── /scripts/                       # Scripts SQL para inicializar o banco
│   └── database_config.py              # Configurações do banco de dados (para integração com Django)
│
├── /versionamento/                     # Controle de versão do código (Git)  
│   ├── .gitignore                      # Arquivo que define o que será ignorado pelo Git
│   └── README.md                       # Arquivo de documentação do projeto
├── .git/                               # Diretório do git
└── requirements.txt                    # Dependências do Python (Django, MySQL, etc)

```

## Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/MyLibrary.git
cd MyLibrary
```

### 2. Configurar o Ambiente Virtual

Crie e ative o ambiente virtual para o projeto:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale as dependências do projeto usando o `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar o Banco de Dados

No arquivo `settings.py` do Django, configure a conexão com o banco de dados MySQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'livros_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Realizar as Migrações

Execute as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### 6. Iniciar o Servidor de Desenvolvimento

Por fim, inicie o servidor Django:

```bash
python manage.py runserver
```

Agora, o sistema estará rodando em `http://127.0.0.1:8000`.

## Estrutura de Banco de Dados

O banco de dados é organizado com as seguintes tabelas principais:

- **Livro**: Contém informações sobre cada livro, como título, autor, assunto, temas, localização (estante e seção) e status (disponível/emprestado).
- **Autor**: Relacionado ao autor de cada livro.
- **Status**: Define se o livro está disponível ou emprestado.

## Contribuindo

Se você quiser contribuir para o projeto, fique à vontade para abrir issues ou pull requests. Para instalar o ambiente de desenvolvimento, siga os passos descritos acima.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações ou dúvidas, entre em contato comigo via email ou pela seção de issues deste repositório.

Email: luiz.contato1364@gmail.com

LinkedIn: www.linkedin.com/in/LuizHenriqueMirandaSantos
```

### **Explicação do README**

- **Descrição**: Um resumo claro do que o projeto faz e suas funcionalidades.
- **Tecnologias Utilizadas**: Lista das tecnologias usadas no projeto.
- **Estrutura do Projeto**: Organiza as pastas e arquivos, facilitando a navegação pelo código.
- **Como Executar o Projeto**: Passo a passo para rodar o projeto localmente.
- **Banco de Dados**: Descrição das tabelas e estrutura.
- **Contribuições**: Orientação para quem quiser ajudar no desenvolvimento do projeto.
- **Licença e Contato**: Informação sobre a licença do projeto e como entrar em contato.
```

##

# MyLibrary In English
MyLibrary is a system for managing your book collection. Register, filter, and view books by title, author, subject, status, and location. The tool allows you to easily manage your personal library, keeping a clear and accessible record of all available books.


![MyLibrary In English](https://github.com/user-attachments/assets/24f96b37-30ed-4081-98a2-361cd1db3d36)



```markdown
# Organized Books - Book Management System

This is a project to organize and manage a home book collection. The system allows registering books, filtering by author,
subject, status (available, borrowed), location (shelf and section), and tracking the availability of each book.

## Technologies Used

- **Backend**:
  - **Python 3.x** with **Django** (for API development and database management)
  - **MySQL** (for the database)
  - **AJAX** (for asynchronous requests on the front-end)

- **Frontend**:
  - **HTML5**, **CSS3** (for page structuring and styling)
  - **Bootstrap 5** (CSS framework for responsive and modern design)
  - **JavaScript** (for interactivity and AJAX requests)

- **Versioning**:
  - **Git** (for version control)

## Features

- **Book Registration**: Allows adding information about books, such as title, author, subject, themes, and location.
- **Book Filtering**: Books can be filtered by subject, author, status (available or borrowed), and location.
- **Status Change**: The book's status can be changed to "borrowed" or "available".
- **Details View**: Displays detailed information about each book, such as author, themes, location, and status.

## Project Structure

The project is organized as follows:


```

### 0. The project is organized as follows:

```markdown
/Mylibrary/                     # Main project directory
│
├── /backend/                            # Server-side code (Django)
│   ├── /books/                         # Django app to manage books
│   │   ├── /migrations/                 # Database migration files
│   │   ├── /templates/                  # Backend HTML templates (if needed to render views)
│   │   ├── /static/                    # Static files (CSS, JS, images)
│   │   ├── admin.py                    # Admin panel configuration
│   │   ├── models.py                   # Database models (Book, User, etc)
│   │   ├── views.py                    # Views to handle API requests
│   │   ├── serializers.py              # Data serialization (converts between objects and JSON)
│   │   ├── urls.py                     # App URLs
│   │   └── forms.py                    # Forms for adding/editing books
│   ├── /config/                        # Django settings
│   │   ├── settings.py                 # Main settings (database, instances)
│   │   ├── urls.py                     # Main backend URLs
│   │   └── wsgi.py                     # Web server entry point
│   ├── manage.py                       # Django management command
│
├── /frontend/                           # Client-side code (HTML, CSS, JS, Bootstrap)
│   ├── /assets/                        # Static files for the front-end (images, fonts)
│   ├── /js/                            # JavaScript files (AJAX for API communication)
│   ├── /css/                           # CSS files (page styles)
│   ├── index.html                      # Home page displaying books
│   ├── register.html                   # Book registration page
│   └── details.html                   # Book details page
│
├── /database/                           # Database (MySQL)
│   ├── /scripts/                       # SQL scripts to initialize the database
│   └── database_config.py              # Database configuration (for integration with Django)
│
├── /versioning/                         # Version control (Git)
│   ├── .gitignore                      # File defining what Git will ignore
│   └── README.md                       # Project documentation file
├── .git/                               # Git directory
└── requirements.txt                    # Python dependencies (Django, MySQL, etc)

```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MyLibrary.git
cd MyLibrary
```

### 2. Set Up the Virtual Environment

Create and activate the virtual environment for the project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the project dependencies using the `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

In the `settings.py` file of Django, configure the connection to the MySQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'books_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations

Run the migrations to set up the database:

```bash
python manage.py migrate
```

### 6. Start the Development Server

Finally, start the Django server:

```bash
python manage.py runserver
```

Now, the system will be running at `http://127.0.0.1:8000`.

## Database Structure

The database is organized with the following main tables:

- **Book**: Contains information about each book, such as title, author, subject, themes, location (shelf and section), and status (available/borrowed).
- **Author**: Related to the author of each book.
- **Status**: Defines whether the book is available or borrowed.

## Contributing

If you'd like to contribute to the project, feel free to open issues or pull requests. To set up the development environment, follow the steps described above.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.

## Contact

For more information or questions, feel free to contact me via email or through the issues section of this repository.

Email: luiz.contato1364@gmail.com

LinkedIn: www.linkedin.com/in/LuizHenriqueMirandaSantos
```

---

### **Explanation of the README**

- **Description**: A clear summary of what the project does and its features.
- **Technologies Used**: List of technologies used in the project.
- **Project Structure**: Organizes folders and files, making it easy to navigate through the code.
- **How to Run the Project**: Step-by-step instructions to run the project locally.
- **Database**: Description of the tables and structure.
- **Contributions**: Guidelines for those who want to contribute to the project.
- **License and Contact**: Information about the project’s license and how to contact you.


