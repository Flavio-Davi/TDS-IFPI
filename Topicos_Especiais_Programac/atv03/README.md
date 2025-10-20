academic-social/
 ├── backend/
 │    ├── infra/
 │    │    ├── db_connection.py       # conexão com o MySQL
 │    │    └── repository_usuario.py  # SQL puro para tabela usuario
 │    ├── service/
 │    │    ├── usuario_service.py     # regras de negócio (ex: validar login)
 │    │    ├── post_service.py
 │    │    └── amizade_service.py
 │    ├── utils/
 │    │    └── helpers.py
 │    └── __init__.py
 │
 ├── frontend/
 │    ├── controller/
 │    │    ├── usuario_controller.py  # chama o service e retorna resultado
 │    │    └── post_controller.py
 │    ├── gui/
 │    │    ├── login_view.py          # interface de login
 │    │    ├── home_view.py
 │    │    └── post_view.py
 │    └── main.py                     # ponto de entrada do app
 │
 ├── .env                             # credenciais do MySQL
 ├── requirements.txt
 └── README.md
