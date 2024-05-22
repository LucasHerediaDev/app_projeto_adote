app_projeto_adote
Projeto Django: Adote um Amigo
O projeto "Adote um Amigo" é uma plataforma desenvolvida em Django que tem como objetivo criar um portal onde usuários podem se registrar e escolher um animal para adoção. Este projeto visa facilitar o processo de adoção de animais, conectando pessoas interessadas em adotar com animais que estão disponíveis para encontrar um novo lar.

Funcionalidades Principais
Registro de Usuários: Permite que novos usuários criem contas para acessar a plataforma.
Autenticação de Usuários: Oferece login seguro para usuários registrados.
Listagem de Animais: Mostra uma lista de animais disponíveis para adoção, com informações detalhadas sobre cada um.
Filtro de Busca: Permite que usuários filtrem animais por categoria, como espécie, idade, tamanho, etc.
Formulário de Adoção: Usuários podem expressar interesse em adotar um animal por meio de um formulário.
Tecnologias Utilizadas
Django 3.x ou 4.x: Framework web em Python.
SQLite: Banco de dados padrão para desenvolvimento (pode ser substituído por PostgreSQL, MySQL, etc. em produção).
Bootstrap: Framework front-end para estilização e design responsivo.
HTML/CSS/JavaScript: Para estrutura e interação da interface.
Passos para Configuração do Ambiente
Clonar o Repositório

bash
Copy code
git clone https://github.com/usuario/app_projeto_adote.git
cd app_projeto_adote
Criar e Ativar um Ambiente Virtual

bash
Copy code
python3 -m venv venv
source venv/bin/activate    # No Windows: venv\Scripts\activate
Instalar Dependências

bash
Copy code
pip install -r requirements.txt
Aplicar Migrações ao Banco de Dados

bash
Copy code
python manage.py migrate
Executar o Servidor de Desenvolvimento

bash
Copy code
python manage.py runserver
Acessar a Aplicação

Abra o navegador e vá para http://127.0.0.1:8000/ para acessar a aplicação.
