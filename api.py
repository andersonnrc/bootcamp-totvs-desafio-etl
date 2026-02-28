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

def obter_conexao():
    """Cria a engine de conexão com o SQL Server."""
    senha_codificada = urllib.parse.quote_plus(DB_CONFIG['password'])
    string_conexao = (
        f"mssql+pyodbc://{DB_CONFIG['user']}:{senha_codificada}"
        f"@{DB_CONFIG['server']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )
    return create_engine(string_conexao)

# ==========================================
# 2. ENDPOINT DA API
# ==========================================
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    """Consulta o banco de dados e retorna a lista de usuários em JSON."""
    try:
        engine = obter_conexao()
        
        # Leitura dos dados com Pandas
        df = pd.read_sql("SELECT id, nome FROM tb_usuarios", engine)
        
        # Conversão para lista de dicionários (padrão JSON)
        usuarios_json = df.to_dict(orient='records')
        
        return jsonify(usuarios_json), 200
        
    except Exception as e:
        print(f"Erro na API: {e}")
        return jsonify({"erro": "Falha ao conectar ou consultar o banco de dados."}), 500

# ==========================================
# 3. EXECUÇÃO DO SERVIDOR
# ==========================================
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
