import pytest
from unittest.mock import Mock
from src.core.dependency_container import DependencyContainer
from src.core.interfaces import IPortfolioService

@pytest.fixture
def mock_portfolio_service():
    """Mock do serviço de portfólio"""
    return Mock(spec=IPortfolioService)

@pytest.fixture
def container(mock_portfolio_service):
    """Fixture que fornece uma instância limpa do container"""
    DependencyContainer._instance = None
    DependencyContainer._services = {}
    container = DependencyContainer()
    container.register_service("portfolio", mock_portfolio_service)
    return container

def test_singleton_pattern(container):
    """Testa se o padrão Singleton está funcionando corretamente"""
    container2 = DependencyContainer()
    assert container is container2

def test_get_service(container, mock_portfolio_service):
    """Testa a recuperação de serviços"""
    portfolio = container.get_service("portfolio")
    assert portfolio is mock_portfolio_service

def test_register_new_service(container):
    """Testa o registro de um novo serviço"""
    mock_service = Mock()
    container.register_service("test", mock_service)
    assert container.get_service("test") is mock_service

def test_nonexistent_service(container):
    """Testa a tentativa de recuperar um serviço inexistente"""
    assert container.get_service("nonexistent") is None