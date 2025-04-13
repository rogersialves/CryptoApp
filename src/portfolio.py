import json
from pathlib import Path
from kivy.logger import Logger
from datetime import datetime
from decimal import Decimal

class Portfolio:
    """Gerenciador de portfolio de criptomoedas"""
    
    def __init__(self, filename="crypto_data.json"):
        self.filename = filename
        self._coins = {"coins": []}
        self.holdings = {}
        self.transactions = []
        self.load_data()
    
    def load_data(self):
        """Carrega dados do arquivo"""
        try:
            filepath = Path(self.filename)
            if filepath.exists():
                Logger.info(f"Carregando dados de {self.filename}")
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        self._coins = data
                    else:
                        Logger.warning("Formato de dados inválido")
                    self.holdings = data.get('holdings', {})
                    self.transactions = data.get('transactions', [])
            else:
                Logger.info(f"Arquivo {self.filename} não encontrado. Criando novo.")
                self.save_data()
                
        except json.JSONDecodeError as e:
            Logger.error(f"Erro ao carregar dados: {str(e)}")
            Logger.info("Criando novo arquivo de dados")
            self.save_data()
        except Exception as e:
            Logger.error(f"Erro ao carregar dados: {str(e)}")
            self._coins = {"coins": []}
            self.holdings = {}
            self.transactions = []
    
    def save_data(self):
        """Salva dados no arquivo"""
        try:
            with open(self.filename, 'w') as f:
                json.dump({
                    'holdings': self.holdings,
                    'transactions': self.transactions,
                    'last_update': datetime.now().isoformat()
                }, f, indent=4)
        except Exception as e:
            Logger.error(f"Erro ao salvar dados: {str(e)}")
    
    def add_transaction(self, symbol: str, amount: Decimal, price: Decimal) -> None:
        """Adiciona uma nova transação ao portfolio."""
        if amount <= 0:
            raise ValueError("O valor da transação deve ser maior que zero")

        symbol = symbol.upper()
        transaction = {
            'id': len(self.transactions) + 1,
            'date': datetime.now().isoformat(),
            'symbol': symbol,
            'amount': str(amount),
            'price': str(price),
            'total': str(amount * price)
        }
        
        self.transactions.append(transaction)
        
        if symbol not in self.holdings:
            self.holdings[symbol] = {'amount': Decimal('0'), 'avg_price': Decimal('0')}
        
        self.holdings[symbol]['amount'] += amount
        
        # Atualiza o preço médio
        total_amount = self.holdings[symbol]['amount']
        total_value = sum(Decimal(t['total']) for t in self.transactions if t['symbol'] == symbol)
        self.holdings[symbol]['avg_price'] = total_value / total_amount if total_amount > 0 else Decimal('0')
        
        # Salva os dados
        self.save_data()
    
    def get_portfolio_summary(self) -> dict:
        """Retorna um resumo do portfolio."""
        return {
            'holdings': self.holdings,
            'total_transactions': len(self.transactions),
            'last_update': datetime.now().isoformat()
        }
    
    def get_coins(self):
        """Retorna lista de moedas"""
        return list(self.holdings.keys())