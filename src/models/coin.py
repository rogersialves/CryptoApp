from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class Coin:
    """Representa uma criptomoeda no portfolio"""
    symbol: str
    name: str
    amount: Decimal
    price: Optional[Decimal] = None
    
    @property
    def value(self) -> Decimal:
        """Calcula o valor total da moeda"""
        if self.price is None:
            return Decimal('0')
        return self.amount * self.price
    
    def add_amount(self, amount: Decimal) -> None:
        """Adiciona uma quantidade à moeda"""
        self.amount += amount
    
    def remove_amount(self, amount: Decimal) -> bool:
        """Remove uma quantidade da moeda se possível"""
        if amount > self.amount:
            return False
        self.amount -= amount
        return True
    
    def update_price(self, new_price: Decimal) -> None:
        """Atualiza o preço da moeda"""
        self.price = new_price