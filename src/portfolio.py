from typing import Dict, Optional
from decimal import Decimal
import json
from pathlib import Path
from kivy.logger import Logger
from datetime import datetime

class Portfolio:
    """Gerenciador de portfolio de criptomoedas"""
    
    def __init__(self, file_path: Optional[Path | str] = None):
        """
        Inicializa um novo portfolio
        Args:
            file_path: Caminho opcional para o arquivo de dados
        """
        self.holdings: Dict[str, Decimal] = {}
        self.file_path = Path(file_path) if file_path else Path("data/portfolio.json")
        self.transactions = []
        self.load()
    
    def add_coin(self, symbol: str, amount: Decimal) -> None:
        """Adiciona uma moeda ao portfolio."""
        if symbol in self.holdings:
            self.holdings[symbol] += amount
        else:
            self.holdings[symbol] = amount
        self.save()
    
    def remove_coin(self, symbol: str, amount: Decimal) -> bool:
        """Remove uma moeda do portfolio."""
        if symbol not in self.holdings:
            return False
        
        if self.holdings[symbol] < amount:
            return False
            
        self.holdings[symbol] -= amount
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        
        self.save()
        return True
    
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
            self.holdings[symbol] = Decimal('0')
        
        self.holdings[symbol] += amount
        
        # Salva os dados
        self.save()
    
    def save(self) -> None:
        """Salva dados no arquivo."""
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = {
                "holdings": {k: str(v) for k, v in self.holdings.items()},
                "transactions": self.transactions,
                "last_update": datetime.now().isoformat()
            }
            with self.file_path.open('w') as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            Logger.error(f"Erro ao salvar dados: {str(e)}")
    
    def load(self) -> None:
        """Carrega dados do arquivo."""
        try:
            if self.file_path.exists():
                with self.file_path.open() as f:
                    data = json.load(f)
                    if not isinstance(data, dict):
                        raise ValueError("Erro ao carregar arquivo")
                        
                    holdings_str = data.get('holdings', {})
                    self.holdings = {
                        k: Decimal(str(v)) for k, v in holdings_str.items()
                    }
                    self.transactions = data.get('transactions', [])
            else:
                self.holdings = {}
                self.transactions = []
                self.save()
        except json.JSONDecodeError:
            Logger.error("Erro ao carregar arquivo")
            raise ValueError("Erro ao carregar arquivo")
        except Exception as e:
            Logger.error(f"Erro ao carregar dados: {str(e)}")
            raise ValueError("Erro ao carregar arquivo")
    
    def get_portfolio_summary(self) -> dict:
        """Retorna um resumo do portfolio."""
        return {
            'holdings': self.holdings,
            'total_transactions': len(self.transactions),
            'last_update': datetime.now().isoformat()
        }
    
    def get_coins(self):
        """Retorna lista de moedas."""
        return list(self.holdings.keys())