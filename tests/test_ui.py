import pytest
from kivy.clock import Clock
from kivy.base import EventLoop
from decimal import Decimal
from src.ui import CryptoAppUI
from src.portfolio import Portfolio
import asyncio
from unittest.mock import Mock
from src.ui.screens import MainScreen  # Agora importa do pacote screens
from src.core.app_state import AppState
from kivymd.uix.screen import MDScreen
from src.core.theme import FONTS

@pytest.fixture
def app():
    """Fixture que fornece uma instância da UI"""
    EventLoop.ensure_window()
    portfolio = Portfolio("test_ui.json")
    return CryptoAppUI(portfolio=portfolio)

def test_ui_initialization(app):
    """Testa inicialização da UI"""
    assert app.portfolio is not None
    assert hasattr(app, 'symbol_input')
    assert hasattr(app, 'amount_input')
    assert hasattr(app, 'price_input')

def test_add_transaction_via_ui(app):
    """Testa adição de transação via UI"""
    # Configura entrada
    app.symbol_input.text = "BTC"
    app.amount_input.text = "1.5"
    app.price_input.text = "50000"
    
    # Executa ação
    app.add_button.trigger_action()
    
    # Verifica resultado
    coins = app.portfolio.get_coins()
    assert len(coins) > 0
    
    coin = app.parse_coin_data(coins[0])
    assert coin.symbol == "BTC"
    assert coin.amount == Decimal("1.5")
    assert coin.avg_price == Decimal("50000")

def test_invalid_input_handling(app):
    """Testa tratamento de entradas inválidas"""
    # Testa entrada vazia
    app.symbol_input.text = ""
    app.amount_input.text = "1.5"
    app.price_input.text = "50000"
    app.add_transaction(None)
    
    # Verifica se mensagem de erro foi exibida
    assert "Erro" in app.status_label.text

def test_ui_update(app):
    """Testa atualização da UI"""
    app.portfolio.add_transaction("ETH", Decimal("2.0"), Decimal("3000"))
    app.update_view()
    
    display_text = app.holdings_label.text
    assert "ETH" in display_text
    assert "2.0" in display_text
    assert "3000" in display_text

def test_clear_inputs(app):
    """Testa limpeza dos campos de entrada"""
    app.symbol_input.text = "BTC"
    app.amount_input.text = "1.0"
    app.price_input.text = "50000"
    
    app.clear_inputs()
    
    assert app.symbol_input.text == ""
    assert app.amount_input.text == ""
    assert app.price_input.text == ""

@pytest.mark.asyncio
async def test_ui_initialization(kivy_app):
    """Testa inicialização da UI"""
    screen = MainScreen()
    assert isinstance(screen, MDScreen)
    assert hasattr(screen, 'amount_input')
    assert hasattr(screen, 'error_label')

@pytest.mark.asyncio
async def test_invalid_amount(kivy_app, event_loop):
    """Testa validação de quantidade inválida"""
    screen = MainScreen()
    
    # Testa valor inválido
    screen.amount_input.text = "abc"
    result = await screen.validate_amount()
    
    assert result is False
    assert screen.error_label.text == "Quantidade inválida"
    assert screen.error_label.theme_text_color == "Error"