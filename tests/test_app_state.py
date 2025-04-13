import pytest
from src.core.app_state import AppState
from src.core.portfolio_state import PortfolioState

def test_app_state_initialization():
    """Testa a inicialização correta do AppState"""
    state = AppState()
    assert isinstance(state.portfolio, PortfolioState)
    assert state.selected_coin is None
    assert len(state.favorites) == 0
    assert len(state.settings) == 0

def test_app_state_reset():
    """Testa o reset do estado"""
    state = AppState()
    state.selected_coin = "BTC"
    state.favorites.append("ETH")
    state.settings["theme"] = "dark"
    
    state.reset()
    
    assert state.selected_coin is None
    assert len(state.favorites) == 0
    assert len(state.settings) == 0