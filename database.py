import json
import urllib.parse
from sqlalchemy import create_engine

def criar_engine(caminho_config='db_config.json', **kwargs):
    """
    Lê as configurações do banco e retorna a engine do SQLAlchemy.
    Aceita parâmetros adicionais (kwargs) para customizar a engine.
    """
    # Lê as credenciais do arquivo JSON
    with open(caminho_config, 'r') as f:
        config = json.load(f)

    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={config['server']},{config['port']};"
        f"DATABASE={config['database']};"
        f"UID={config['user']};"
        f"PWD={config['password']};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )

    string_conexao = f"mssql+pyodbc:///?odbc_connect={params}"

    # Configurações padrão de pool (podem ser sobrescritas/estendidas pelos kwargs)
    opcoes_engine = {
        'pool_pre_ping': True,
        'pool_size': 5,
        'max_overflow': 10
    }
    opcoes_engine.update(kwargs) # Mescla os parâmetros extras passados

    return create_engine(string_conexao, **opcoes_engine)
