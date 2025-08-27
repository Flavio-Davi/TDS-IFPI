# 🗨️ Chat em Tempo Real - Projeto Integrador

Este repositório contém o projeto integrador do curso **Técnico em Desenvolvimento de Sistemas** do **Instituto Federal do Piauí (IFPI)**. O objetivo do projeto é o desenvolvimento de um **chat em tempo real** utilizando tecnologias modernas tanto no backend quanto no frontend.

## 🎯 Objetivo

Criar uma aplicação de chat em tempo real onde múltiplos usuários podem interagir de forma simultânea, com uma interface web amigável e um backend robusto, utilizando tecnologias modernas de mercado.

## 🛠️ Tecnologias Utilizadas

- **Python** - Lógica de backend
- **Go (Golang)** - Comunicação em tempo real / performance
- **FastAPI** - Framework backend em Python
- **SQLAlchemy** - ORM para comunicação com o banco de dados
- **MySQL** - Banco de dados relacional
- **HTML5 & CSS3** - Estrutura e estilo do frontend
- **JavaScript (Vanilla)** - Funcionalidade dinâmica do frontend

## 📁 Estrutura do Projeto (provisória)

chat-tempo-real/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ └── chat_handler.go
├── frontend/
│ ├── index.html
│ ├── styles.css
│ └── script.js
├── requirements.txt
└── README.md

## 🚀 Como Executar (passos iniciais)

> **Pré-requisitos:** Python 3.10+, Go, MySQL

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/chat-tempo-real.git
   cd chat-tempo-real
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
  uvicorn backend.main:app --reload
  go run backend/chat_handler.go
  http://localhost:8000
## 👥 Autores

Flávio Davi - https://github.com/Flavio-Davi
Italo Bruno - https://github.com/italobr02
