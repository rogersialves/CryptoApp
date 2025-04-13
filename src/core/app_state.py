from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from decimal import Decimal
from .portfolio_state import PortfolioState

@dataclass
class AppState:
    """Estado global da aplicação"""
    portfolio: PortfolioState = field(default_factory=PortfolioState)
    selected_coin: Optional[str] = None
    favorites: List[str] = field(default_factory=list)
    settings: Dict[str, Any] = field(default_factory=dict)

    def reset(self) -> None:
        """Reseta o estado para valores padrão"""
        self.portfolio = PortfolioState()
        self.selected_coin = None
        self.favorites.clear()
        self.settings.clear()