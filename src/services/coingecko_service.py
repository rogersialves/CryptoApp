import requests
import time
from kivy.logger import Logger

class CoinGeckoService:
    """Serviço para interação com a API do CoinGecko"""
    
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
    
    def get_top_coins(self, limit=20):
        """Obtém as top criptomoedas por market cap"""
        endpoint = f"{self.base_url}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }
        
        for _ in range(3):  # Tenta 3 vezes
            try:
                response = requests.get(endpoint, params=params)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                Logger.error(f"Erro na API: {e}")
                time.sleep(1)  # Aguarda antes de tentar novamente
        return []