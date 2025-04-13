from datetime import datetime
from decimal import Decimal
from .data_manager import DataManager
import logging

class Portfolio:
    def __init__(self, data_file="crypto_data.json"):
        self.data_manager = DataManager(data_file)
        self._load_data()
    
    def _load_data(self):
        """Carrega dados do arquivo"""
        data = self.data_manager.load_data()
        if data is None:
            raise ValueError("Erro ao carregar arquivo")
        self.holdings = data.get('holdings', {})
        self.transactions = data.get('transactions', [])
    
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
        self._save_data()
    
    def _save_data(self):
        """Salva os dados atuais no arquivo"""
        return self.data_manager.save_data({
            'holdings': self.holdings,
            'transactions': self.transactions,
            'last_update': datetime.now().isoformat()
        })

    def get_portfolio_summary(self) -> dict:
        """Retorna um resumo do portfolio."""
        return {
            'holdings': self.holdings,
            'total_transactions': len(self.transactions),
            'last_update': datetime.now().isoformat()
        }