import requests
from kivy.logger import Logger

class CoinGeckoService:
    """Serviço para interação com a API do CoinGecko"""
    
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"
    
    def get_top_coins(self, limit=20):
        """Obtém as top criptomoedas por market cap"""
        try:
            endpoint = f"{self.base_url}/coins/markets"
            params = {
                "vs_currency": "usd",
                "order": "market_cap_desc",
                "per_page": limit,
                "page": 1,
                "sparkline": False
            }
            
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
            
        except Exception as e:
            Logger.error(f"Erro ao obter dados do CoinGecko: {str(e)}")
            return []