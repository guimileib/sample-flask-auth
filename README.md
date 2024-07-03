# Flask User Management API

Este projeto é uma API de gerenciamento de usuários usando Flask, Flask-Login e SQLAlchemy.

## Requisitos

- Python 3.x
- Flask
- Flask-Login
- Flask-SQLAlchemy

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu_usuario/seu_repositorio.git
    cd seu_repositorio
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicialize o banco de dados:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

## Configuração

Atualize o arquivo de configuração com sua chave secreta e o URI do banco de dados:

```python
app.config['SECRET_KEY'] = "sua_chave_secreta"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
```

## Uso

```python
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
```
## Rotas

- URL: `/login `

- Método: ` POST `

- Descrição: Autentica o usuário.

- Exemplo de corpo de requisição:

  ```json
  {
    "username": "seu_username",
    "password": "sua_password"
  }
  ```

## Logout
  
- URL: `/logout`
- Método: GET
- Descrição: Realiza logout do usuário autenticado.

## Criar Usuário
- URL: `/user`

- Método: `POST`

- Descrição: Cria um novo usuário.

- Exemplo de corpo de requisição:

  ```json
  {
    "username": "novo_username",
    "password": "nova_password"
  }
  ```

## Ler Usuário

- **URL**: `/user/<int:id_user>`
- **Método**: `GET`
- **Descrição**: Retorna os dados de um usuário específico.
- **Resposta de exemplo**:

    ```json
    {
        "username": "username"
    }
    ```

## Atualizar Usuário

- **URL**: `/user/<int:id_user>`
- **Método**: `PUT`
- **Descrição**: Atualiza a senha de um usuário específico.
- **Exemplo de corpo de requisição**:

    ```json
    {
        "password": "nova_password"
    }
    ```

## Deletar Usuário

- **URL**: `/user/<int:id_user>`
- **Método**: `DELETE`
- **Descrição**: Deleta um usuário específico.

## Inicialização do Servidor

Para iniciar o servidor, execute:

```bash
flask run
```

## Estrutura do Projeto

```plaintext
.
├── app.py
├── models
│   └── user.py
├── database.py
├── requirements.txt
└── README.md

```
## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob os termos da licença MIT.

## Autor

Criado por [guimileib](https://github.com/guimileib)

---


  

  

  


