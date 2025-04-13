import pytest
import sys
import os
from decimal import Decimal
from datetime import datetime
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.portfolio import Portfolio
from src.data_manager import DataManager

# Constantes para testes
TEST_SYMBOLS = {
    "BTC": {"amount": "1.5", "price": "50000"},
    "ETH": {"amount": "2.0", "price": "3000"},
}

@pytest.fixture
def test_file():
    """Fixture que fornece o nome do arquivo de teste"""
    return "test_crypto_data.json"

@pytest.fixture
def test_portfolio(test_file):
    """Fixture que fornece um portfolio de teste limpo"""
    if os.path.exists(test_file):
        os.remove(test_file)
    
    portfolio = Portfolio(test_file)
    
    yield portfolio
    
    if os.path.exists(test_file):
        os.remove(test_file)

@pytest.fixture
def populated_portfolio(test_portfolio):
    """Fixture que fornece um portfolio com dados"""
    for symbol, data in TEST_SYMBOLS.items():
        test_portfolio.add_transaction(
            symbol, 
            Decimal(data["amount"]), 
            Decimal(data["price"])
        )
    return test_portfolio

@pytest.fixture
def temp_portfolio(tmp_path):
    """Fixture que cria um portfolio temporário para testes"""
    portfolio_file = tmp_path / "test_portfolio.json"
    return Portfolio(file_path=portfolio_file)

@pytest.fixture
def sample_portfolio(tmp_path):
    """Fixture que cria um portfolio de teste"""
    portfolio = Portfolio(file_path=tmp_path / "test_portfolio.json")
    return portfolio

def test_add_transaction(test_portfolio):
    test_portfolio.add_transaction("BTC", Decimal("1.5"), Decimal("50000"))
    assert "BTC" in test_portfolio.holdings
    assert test_portfolio.holdings["BTC"]["amount"] == Decimal("1.5")
    assert len(test_portfolio.transactions) == 1

def test_portfolio_persistence(test_portfolio, test_file):
    """Testa se os dados são persistidos corretamente"""
    # Limpa o arquivo de teste se existir
    if os.path.exists(test_file):
        os.remove(test_file)
    
    # Cria um novo portfolio com o arquivo de teste
    portfolio = Portfolio(test_file)
    
    # Adiciona uma transação
    portfolio.add_transaction("ETH", Decimal("2.0"), Decimal("3000"))
    
    # Cria uma nova instância usando o mesmo arquivo
    new_portfolio = Portfolio(test_file)
    
    # Verifica se os dados foram carregados corretamente
    assert "ETH" in new_portfolio.holdings, "ETH não encontrado nos holdings"
    assert new_portfolio.holdings["ETH"]["amount"] == Decimal("2.0"), "Valor incorreto para ETH"
    
    # Limpa o arquivo de teste
    if os.path.exists(test_file):
        os.remove(test_file)

def test_portfolio_persistence(sample_portfolio):
    """Testa persistência do portfolio"""
    # Usar Decimal diretamente
    amount = Decimal('1.5')
    sample_portfolio.add_coin("BTC", amount)
    assert sample_portfolio.holdings["BTC"] == amount

def test_invalid_transaction(test_portfolio):
    """Testa o tratamento de transações inválidas"""
    with pytest.raises(ValueError):
        test_portfolio.add_transaction("BTC", Decimal("-1.0"), Decimal("50000"))

def test_get_portfolio_summary(test_portfolio):
    """Testa o resumo do portfolio"""
    test_portfolio.add_transaction("BTC", Decimal("1.0"), Decimal("50000"))
    summary = test_portfolio.get_portfolio_summary()
    
    assert "BTC" in summary["holdings"]
    assert summary["total_transactions"] == 1
    assert "last_update" in summary

def test_multiple_transactions(test_portfolio):
    """Testa múltiplas transações para a mesma moeda"""
    test_portfolio.add_transaction("BTC", Decimal("1.0"), Decimal("50000"))
    test_portfolio.add_transaction("BTC", Decimal("0.5"), Decimal("45000"))
    
    assert test_portfolio.holdings["BTC"]["amount"] == Decimal("1.5")
    # Verifica preço médio: (50000 + 22500) / 1.5
    expected_avg = (Decimal("50000") + Decimal("22500")) / Decimal("1.5")
    assert test_portfolio.holdings["BTC"]["avg_price"] == expected_avg

def test_zero_amount_transaction(test_portfolio):
    """Testa transação com quantidade zero"""
    with pytest.raises(ValueError, match="deve ser maior que zero"):
        test_portfolio.add_transaction("BTC", Decimal("0"), Decimal("50000"))

def test_load_invalid_file():
    """Testa carregamento de arquivo inválido"""
    test_file = "invalid.json"
    
    # Cria um arquivo JSON inválido
    with open(test_file, "w") as f:
        f.write("{invalid_json}")
    
    # Verifica se a exceção é levantada
    with pytest.raises(ValueError, match="Erro ao carregar arquivo"):
        Portfolio(test_file)
    
    # Limpa o arquivo de teste
    if os.path.exists(test_file):
        os.remove(test_file)

def test_portfolio_initialization(temp_portfolio):
    """Testa se o portfolio é inicializado corretamente"""
    assert isinstance(temp_portfolio.holdings, dict)
    assert len(temp_portfolio.holdings) == 0

def test_add_transaction(temp_portfolio):
    """Testa adição de transação"""
    temp_portfolio.add_coin("BTC", Decimal("1.5"))
    assert temp_portfolio.holdings["BTC"] == Decimal("1.5")

def test_multiple_transactions(tmp_portfolio):
    """Testa múltiplas transações"""
    # Usa str para criar Decimal
    amount1 = Decimal('1.5')
    amount2 = Decimal('2.5')
    
    tmp_portfolio.add_coin("BTC", amount1)
    tmp_portfolio.add_coin("BTC", amount2)
    
    assert tmp_portfolio.holdings["BTC"] == amount1 + amount2