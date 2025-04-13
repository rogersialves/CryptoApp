import pytest
from decimal import Decimal
from src.core.portfolio_state import PortfolioState

def test_portfolio_state_initialization():
    """Testa inicialização do estado do portfolio"""
    state = PortfolioState()
    assert len(state.holdings) == 0
    assert state.total_value == Decimal('0')

def test_add_holding():
    """Testa adição de moeda ao portfolio"""
    state = PortfolioState()
    state.add_holding("BTC", Decimal('1.5'))
    assert state.holdings["BTC"] == Decimal('1.5')

def test_remove_holding():
    """Testa remoção de moeda do portfolio"""
    state = PortfolioState()
    state.add_holding("ETH", Decimal('2.0'))
    assert state.remove_holding("ETH", Decimal('1.0'))
    assert state.holdings["ETH"] == Decimal('1.0')