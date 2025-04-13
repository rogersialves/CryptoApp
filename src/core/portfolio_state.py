from dataclasses import dataclass, field
from typing import Dict
from decimal import Decimal

@dataclass
class PortfolioState:
    """Estado do portfolio do usuário"""
    holdings: Dict[str, Decimal] = field(default_factory=dict)
    total_value: Decimal = field(default_factory=lambda: Decimal('0'))
    
    def add_holding(self, symbol: str, amount: Decimal) -> None:
        """Adiciona ou atualiza uma posição no portfolio"""
        if symbol in self.holdings:
            self.holdings[symbol] += amount
        else:
            self.holdings[symbol] = amount
    
    def remove_holding(self, symbol: str, amount: Decimal) -> bool:
        """Remove uma quantidade de uma moeda do portfolio"""
        if symbol not in self.holdings:
            return False
            
        if self.holdings[symbol] < amount:
            return False
            
        self.holdings[symbol] -= amount
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        return True