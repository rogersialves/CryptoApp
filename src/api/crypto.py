"""Módulo para interação com API de criptomoedas"""
from typing import List, Dict, Any
import aiohttp
from kivy.logger import Logger

async def search_crypto(query: str) -> List[Dict[str, Any]]:
    """
    Pesquisa criptomoedas pelo nome/símbolo
    
    Args:
        query: Texto para pesquisa
        
    Returns:
        Lista de resultados no formato:
        [{"symbol": "BTC", "name": "Bitcoin", ...}]
    """
    # TODO: Implementar chamada real à API
    # Mock temporário para testes
    mock_results = [
        {"symbol": "BTC", "name": "Bitcoin"},
        {"symbol": "ETH", "name": "Ethereum"}
    ]
    
    Logger.debug(f"Pesquisando por: {query}")
    return [r for r in mock_results if query.lower() in r["name"].lower()]