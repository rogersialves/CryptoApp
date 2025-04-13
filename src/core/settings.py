from typing import Final
from pathlib import Path

# Project paths
PROJECT_ROOT: Final = Path(__file__).parent.parent.parent
SRC_DIR: Final = PROJECT_ROOT / 'src'
DATA_DIR: Final = PROJECT_ROOT / 'data'

# API Configuration
API_BASE_URL: Final = "https://api.coingecko.com/api/v3"
API_TIMEOUT: Final = 30  # segundos

# App Configuration
DEFAULT_CURRENCY: Final = "USD"
SUPPORTED_CURRENCIES: Final = ["USD", "EUR", "BRL", "BTC", "ETH"]
DEFAULT_THEME: Final = "light"
CACHE_DURATION: Final = 300  # segundos

# UI Configuration
REFRESH_INTERVAL: Final = 60  # segundos
MAX_COINS_DISPLAY: Final = 100
CHART_TIMEFRAMES: Final = ["24h", "7d", "30d", "1y"]

# Error Messages
ERRORS = {
    "api_timeout": "Tempo limite excedido. Tente novamente.",
    "connection_error": "Erro de conexão. Verifique sua internet.",
    "invalid_amount": "Valor inválido. Use apenas números positivos.",
}