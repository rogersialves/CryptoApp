from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict

class IPortfolioService(ABC):
    """Interface para o serviço de portfólio"""
    
    @abstractmethod
    def get_portfolio(self) -> Dict[str, Decimal]:
        """Retorna o portfólio atual"""
        pass
    
    @abstractmethod
    def add_coin(self, symbol: str, amount: Decimal) -> None:
        """Adiciona uma moeda ao portfólio"""
        pass