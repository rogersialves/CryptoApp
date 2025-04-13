import json
import os
from datetime import datetime
from decimal import Decimal
import logging

class DataManager:
    def __init__(self, data_file="crypto_data.json"):
        self.data_file = data_file
        self.ensure_data_file()
        logging.basicConfig(level=logging.INFO)
    
    def ensure_data_file(self):
        """Cria o arquivo de dados se não existir"""
        if not os.path.exists(self.data_file):
            logging.info(f"Criando novo arquivo de dados: {self.data_file}")
            self.save_data({
                'holdings': {},
                'transactions': [],
                'last_update': datetime.now().isoformat()
            })
    
    def load_data(self):
        """Carrega dados do arquivo JSON"""
        try:
            logging.info(f"Carregando dados de: {self.data_file}")
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                
                # Converte strings para Decimal nos holdings
                holdings = {}
                for symbol, values in data.get('holdings', {}).items():
                    holdings[symbol] = {
                        'amount': Decimal(str(values['amount'])),
                        'avg_price': Decimal(str(values['avg_price']))
                    }
                data['holdings'] = holdings
                
                return data
        except json.JSONDecodeError as e:
            logging.error(f"Erro ao decodificar JSON: {e}")
            return None
        except Exception as e:
            logging.error(f"Erro ao carregar dados: {e}")
            return None
    
    def save_data(self, data):
        """Salva dados no arquivo JSON"""
        try:
            logging.info(f"Salvando dados em: {self.data_file}")
            # Converte Decimal para string antes de salvar
            serializable_data = {
                'holdings': {
                    k: {
                        'amount': str(v['amount']),
                        'avg_price': str(v['avg_price'])
                    } for k, v in data['holdings'].items()
                },
                'transactions': data['transactions'],
                'last_update': data['last_update']
            }
            
            # Salva em um arquivo temporário primeiro
            temp_file = f"{self.data_file}.tmp"
            with open(temp_file, 'w') as f:
                json.dump(serializable_data, f, indent=4)
            
            # Renomeia o arquivo temporário para o arquivo final
            if os.path.exists(self.data_file):
                os.replace(temp_file, self.data_file)
            else:
                os.rename(temp_file, self.data_file)
                
            logging.info("Dados salvos com sucesso")
            return True
        except Exception as e:
            logging.error(f"Erro ao salvar dados: {e}")
            if os.path.exists(temp_file):
                os.remove(temp_file)
            return False