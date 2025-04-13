import json
from pathlib import Path

def create_initial_data():
    """Cria arquivo de dados inicial para o CryptoApp"""
    initial_data = {
        "coins": [],
        "version": "1.0"
    }
    
    try:
        data_file = Path('../crypto_data.json')
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, indent=4)
        print("Arquivo de dados criado com sucesso!")
    except Exception as e:
        print(f"Erro ao criar arquivo: {e}")

if __name__ == '__main__':
    create_initial_data()