import logging
from typing import Dict, Any
from src.services.coingecko_service import CoinGeckoService
from src.services.portfolio_service import PortfolioService

class DependencyContainer:
    _instance = None
    _services: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_services()
        return cls._instance

    def _initialize_services(self):
        """Inicializa os serviços principais"""
        self._services["coingecko"] = CoinGeckoService()
        self._services["portfolio"] = PortfolioService()

    def get_service(self, service_name: str) -> Any:
        """Retorna uma instância do serviço solicitado"""
        return self._services.get(service_name)

    def register_service(self, name: str, service: Any) -> None:
        """Registra um novo serviço no container"""
        logging.info(f"Registrando serviço: {name}")
        self._services[name] = service