# Sistema de Cadastro de Clientes com Python e Migração de Dados entre Bancos de Dados

Este projeto permite o cadastro de clientes em um banco de dados SQLite e a migração dos dados para o MySQL. A interface gráfica foi criada com Tkinter, e os dados podem ser exportados para arquivos CSV e Excel. A migração dos dados para o MySQL é realizada usando SQLAlchemy.

## Funcionalidades
* Cadastro de clientes (ID, nome, celular, e-mail, CPF) no banco de dados SQLite.
* Migração automática dos dados de SQLite para MySQL.
* Geração de relatórios em CSV e Excel.
* Interface gráfica simples utilizando Tkinter.

Para que o projeto funcione com o seu banco de dados MySQL, você precisará ajustar as configurações de conexão no código. Siga os passos abaixo:

1. Abra o arquivo do projeto onde está o código Python.
2. Localize a linha de conexão com o banco de dados MySQL (geralmente dentro da função de migração sqlite_to_mysql).

```bash
eng_mysql = create_engine("mysql+mysqlconnector://root:carina123@localhost/clientes")
````
3. Altere as informações de conexão para refletir os dados do seu banco de dados:

* usuário: Substitua pelo seu usuário MySQL.
* senha: Substitua pela sua senha MySQL.
* localhost: Substitua pelo endereço do seu servidor MySQL, se não estiver rodando localmente.
* clientes: Substitua pelo nome do seu banco de dados MySQL.
  
Exemplo:
```bash
eng_mysql = create_engine("mysql+mysqlconnector://seu_usuario:senha@localhost/seu_banco_de_dados")
````

## Como executar o projeto
1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
````
3. Execute o script Python e utilize a interface gráfica para cadastrar os clientes.

## Licença
Este projeto é de código aberto. Fique à vontade para contribuir!


