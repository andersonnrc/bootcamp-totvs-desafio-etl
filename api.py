from flask import Flask, jsonify
import pandas as pd
from database import criar_engine

# ==========================================
# 1. INICIALIZAÇÃO DO FLASK E CONFIGURAÇÕES
# ==========================================
app = Flask(__name__)

# 🔥 Engine global
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
