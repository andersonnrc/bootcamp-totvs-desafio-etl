from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine
import urllib.parse
import json

# ==========================================
# 1. INICIALIZAÇÃO DO FLASK E CONFIGURAÇÕES
# ==========================================
app = Flask(__name__)

# Lê as credenciais do arquivo JSON
with open('db_config.json', 'r') as f:
    DB_CONFIG = json.load(f)

def criar_engine():
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER={DB_CONFIG['server']},{DB_CONFIG['port']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['user']};"
        f"PWD={DB_CONFIG['password']};"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes;"
    )

    string_conexao = f"mssql+pyodbc:///?odbc_connect={params}"

    return create_engine(
        string_conexao,
        pool_pre_ping=True,   # evita conexões mortas
        pool_size=5,          # número de conexões no pool
        max_overflow=10       # conexões extras se necessário
    )

# 🔥 Engine global (criada uma única vez)
engine = criar_engine()

# ==========================================
# 2. ENDPOINT DA API
# ==========================================
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    try:
        df = pd.read_sql("SELECT id, nome FROM tb_usuarios", engine)

        usuarios_json = df.to_dict(orient='records')

        return jsonify(usuarios_json), 200

    except Exception as e:
        print(f"Erro na API: {e}")
        return jsonify({"erro": "Falha ao consultar o banco de dados."}), 500

# ==========================================
# 3. EXECUÇÃO DO SERVIDOR
# ==========================================
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
