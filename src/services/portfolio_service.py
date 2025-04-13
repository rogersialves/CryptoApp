import logging
from decimal import Decimal
from typing import Dict, Optional
from src.core.interfaces import IPortfolioService

class PortfolioService(IPortfolioService):
    def __init__(self):
        self._portfolio: Dict[str, Decimal] = {}
    
    def get_portfolio(self) -> Dict[str, Decimal]:
        return self._portfolio.copy()
    
    def add_coin(self, symbol: str, amount: Decimal) -> None:
        self._portfolio[symbol] = amount
        logging.info(f"Moeda adicionada: {symbol}, quantidade: {amount}")