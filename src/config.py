"""Configurações globais da aplicação"""
from src.core.settings import *
from src.core.theme import *

# Re-exportando configurações principais
__all__ = [
    # De settings.py
    'PROJECT_ROOT',
    'SRC_DIR',
    'DATA_DIR',
    'API_BASE_URL',
    'API_TIMEOUT',
    'DEFAULT_CURRENCY',
    'SUPPORTED_CURRENCIES',
    'DEFAULT_THEME',
    'CACHE_DURATION',
    'REFRESH_INTERVAL',
    'MAX_COINS_DISPLAY',
    'CHART_TIMEFRAMES',
    'ERRORS',
    
    # De theme.py
    'FONTS',
    'STYLES',
    'CARD_STYLE',
    'get_font_style',
    'get_card_style'
]