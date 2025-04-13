import pytest
from kivy.clock import Clock
from kivy.base import EventLoop
from decimal import Decimal
from src.ui import CryptoControlUI
from src.portfolio import Portfolio

@pytest.fixture
def app():
    """Fixture que fornece uma instância da UI"""
    EventLoop.ensure_window()
    portfolio = Portfolio("test_ui.json")
    return CryptoControlUI(portfolio=portfolio)

def test_ui_initialization(app):
    """Testa se a UI inicializa corretamente"""
    assert app.portfolio is not None
    assert hasattr(app, 'symbol_input')
    assert hasattr(app, 'amount_input')
    assert hasattr(app, 'price_input')

def test_add_transaction_via_ui(app):
    """Testa adição de transação via UI"""
    # Simula preenchimento dos campos
    app.symbol_input.text = "BTC"
    app.amount_input.text = "1.5"
    app.price_input.text = "50000"
    
    # Simula clique no botão
    app.add_transaction(None)
    
    # Verifica se a transação foi adicionada
    assert "BTC" in app.portfolio.holdings
    assert app.portfolio.holdings["BTC"]["amount"] == Decimal("1.5")

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
    # Limpa holdings anteriores
    app.portfolio.holdings = {}
    app.portfolio.transactions = []
    
    # Adiciona uma transação
    app.portfolio.add_transaction("ETH", Decimal("2.0"), Decimal("3000"))
    
    # Força atualização da UI manualmente
    app.update_view()
    
    # Verifica se a UI foi atualizada
    assert "ETH" in app.holdings_label.text
    assert "2.0" in app.holdings_label.text
    assert "3000" in app.holdings_label.text

def test_clear_inputs(app):
    """Testa limpeza dos campos de entrada"""
    app.symbol_input.text = "BTC"
    app.amount_input.text = "1.0"
    app.price_input.text = "50000"
    
    app.clear_inputs()
    
    assert app.symbol_input.text == ""
    assert app.amount_input.text == ""
    assert app.price_input.text == ""

def test_invalid_amount(app):
    """Testa entrada de quantidade inválida"""
    app.symbol_input.text = "BTC"
    app.amount_input.text = "abc"  # Valor inválido
    app.price_input.text = "50000"
    
    app.add_transaction(None)
    
    assert "Erro" in app.status_label.text