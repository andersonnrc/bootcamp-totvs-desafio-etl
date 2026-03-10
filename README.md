# 🚀 Pipeline de Dados e IA para Marketing Bancário

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white)
![DBeaver](https://img.shields.io/badge/DBeaver-382923?style=for-the-badge&logo=dbeaver&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Groq](https://img.shields.io/badge/Groq_API-F37A24?style=for-the-badge&logo=groq&logoColor=white)

## 📌 Sobre o Projeto
Este projeto é uma solução *End-to-End* (Ponta a Ponta) que integra Engenharia de Dados, Desenvolvimento Backend (Microsserviço) e Inteligência Artificial Generativa. O objetivo é simular uma esteira automatizada para um banco, onde dados de clientes são extraídos, servidos via API REST e consumidos por uma IA que atua como Especialista em Marketing para gerar campanhas personalizadas de investimentos. O gerenciamento e validação dos dados no SQL Server foram realizados utilizando o DBeaver.

## 🏗️ Arquitetura da Solução

O projeto foi construído de forma modularizada e desacoplada, utilizando **Docker** para isolamento do banco de dados, e está dividido em três fases principais:

1. **Fase 1: ETL e Carga (Jupyter Notebook)**
   - Processamento de dados brutos utilizando `pandas`.
   - Carga idempotente dos dados em um banco relacional **SQL Server (rodando em container Docker)** utilizando `sqlalchemy` e `pyodbc`.
2. **Fase 2: API REST (Flask)**
   - Microsserviço independente (`api.py`) que consulta o banco de dados.
   - Disponibiliza os dados dos clientes em formato JSON no endpoint `/api/usuarios`.
3. **Fase 3: Consumo e Geração com IA Generativa (Jupyter Notebook)**
   - Consumo da API REST local via pacote `requests`.
   - Integração com a **API da Groq** (utilizando o modelo de baixíssima latência `llama-3.1-8b-instant`).
   - Geração de mensagens de marketing hiper-personalizadas baseadas no nome do cliente.
   - Gravação do histórico das mensagens geradas de volta no SQL Server, alimentando a tabela `tb_mensagens_marketing`.

## ⚙️ Pré-requisitos e Configuração

- Python 3.x
- Docker (Desktop ou Engine)
- DBeaver (para administração do banco de dados)
- Microsoft ODBC Driver 17 for SQL Server
- Chave de API da [Groq](https://console.groq.com/).

### 1. Subindo o Banco de Dados (Docker)
Antes de rodar a aplicação, inicie o container do SQL Server executando o comando abaixo no seu terminal:
```bash
docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=Sqls3rv3r!" -p 1433:1433 --name sqlserver --hostname sqlserver -d mcr.microsoft.com/mssql/server:2022-latest
```

### 2. Criando o Banco de Dados no DBeaver
Após configurar as conexões de acesso no DBeaver, basta criar um banco de dados chamado `dioBootcamp`.

### 3. Criando ambiente virtual e instalando pacotes via `pip`
Executar comando através da instrução a seguir para criar ambiente virtual:
```bash
python -m venv DIO_Bootcamp_Totvs_IA
```
Executar comando a seguir para ativar ambiente virtual:
```bash
DIO_Bootcamp_Totvs_IA\Scripts\activate
```
Executar comando a seguir para instalar pacotes necessários para as aplicações deste projeto:
```bash
pip install -r requirements.txt
```
### 4. Instalando o driver oficial da Microsoft para o SQL Server

Para este mini-projeto, foi utilizado o Windows 11. Então antes da execução das aplicações, será necessário instalar o driver oficial da Microsoft: `Microsoft ODBC Driver 17 for SQL Server`. Importante lembrar que já existe uma versão mais atual desse driver. Caso seja instalada a versão 18, será necessário alterar a versão nos códigos onde estão as configurações de conexão do banco de dados.

## 🚀 Execução das aplicações

### 1. Executar a carga dos dados

Executar no terminal o comando a seguir para acessar scripts do Jupyter Notebook:
```bash
jupyter notebook
```
Caso o Jupyter Notebook não abra, basta digitar em qualquer browser: `localhost:8888`

Com o Jupyter notebook aberto, basta executar todas as células do script `carga_dados.ipynb` cujo resultado é exibido na imagem a seguir:
![](/images/result_exec_load.png "Resultado da carga dos dados")

A próxima etapa é subir a api REST. Para este passo, abra outro terminal na pasta do projeto e execute os mesmos passos para ativação do ambiente virtual `DIO_Bootcamp_Totvs_IA`. Com o ambiente virtual ativado, execute o comando a seguir:
```bash
python api.py
```

O último passo será executar o script `app_ia.ipynb`. É possível que apresente algum erro ao executar todas as células no browser. Para contornar esse problema, será necessário executar o comando a seguir no terminal do ambiente virtual ativado:
```bash
python -m ipykernel install --user --name=DIO_Bootcamp_Totvs_IA --display-name "Python (DIO Bootcamp Totvs IA)"
```
No script do Jupyter Notebook no browser, há uma alteração a ser feita. Acessar a opção `Kernel -> Change Kernel` e escolher a opção `Python (DIO Bootcamp Totvs IA)`.

Após essas configurações, pode executar todas as células do script `app_ia.ipynb` cujo resultado é exibido na imagem a seguir
![](/images/result_exec_ia.png "Resultado da geração das mensagens personalizadas com IA")

## 🧑‍💼 Contato

[Linkedin](https://www.linkedin.com/in/anderson-ribeiro-carvalho)
