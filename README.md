# Projeto Django Conteinerizado com Docker & Docker Compose

Este repositório contém um serviço web desenvolvido em **Django** e inteiramente conteinerizado com **Docker** e **Docker Compose**.

---

## Pré-requisitos

Para executar este projeto em sua máquina local, certifique-se de ter os seguintes componentes instalados:

- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python 3.10+](https://www.python.org/)

---

## Como Rodar a Aplicação com Docker Compose

Siga os passos abaixo para subir a aplicação conteinerizada:

### 1. Clonar o Repositório
```bash
git clone https://github.com/joao2dev/Docker-softex.git
cd Docker-softex
```

### 2. Parar qualquer serviço rodando na porta 8000
Certifique-se de que a porta `8000` não esteja ocupada por outro processo local.

### 3. Construir e Subir o Container
Execute o comando do Docker Compose na raiz do projeto:
```bash
docker-compose up --build
```

### 4. Acessar a Aplicação
Abra o navegador e acesse:
**[http://localhost:8000](http://localhost:8000)**

---

## Estrutura do Projeto

```text
Docker-softex/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── db.sqlite3
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
└── README.md
```

---

## Link do Repositório
Repositório GitHub: **[https://github.com/joao2dev/Docker-softex](https://github.com/joao2dev/Docker-softex)**
