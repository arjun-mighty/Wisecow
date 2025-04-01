# CRUD App

## ENDPOINTS

GET / - returns "Hello"  
POST / - input {"name": "yourname"} and output "Hello yourname"

## HOW TO RUN

Open terminal in crud-app folder.

1. UV(astral)  
   `uv sync`  
   `uv run fastapi run`

2. Docker

- build image  
  `docker build -t crud-app .`
- start a container  
  `docker run -d --name crud-app -p 8000:8000 crud-app`
