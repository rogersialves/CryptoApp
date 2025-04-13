from typing import List
from decimal import Decimal
from kivy.logger import Logger
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from src.core.theme import STYLES, FONTS, get_font_style, get_card_style
from src.core.dependency_container import DependencyContainer
from src.core.app_state import AppState
from src.portfolio import Portfolio
from ..models.coin import Coin  # Assumindo que existe uma classe Coin

class PortfolioScreen(MDScreen):
    """Tela de portfolio do usuário"""
    
    def __init__(self, portfolio_manager: Portfolio, **kwargs):
        super().__init__(**kwargs)
        self.portfolio = portfolio_manager
        self.app_state = AppState()
        
    def on_enter(self):
        """Chamado quando a tela é exibida"""
        self.update_portfolio_view()
        
    def update_portfolio_view(self):
        """Atualiza a visualização do portfolio"""
        holdings = self.app_state.portfolio.holdings
        for symbol, amount in holdings.items():
            coin = self.portfolio.get_coin(symbol)
            if coin:
                self.add_coin_to_list(coin, amount)

class CoinListItem(MDCard):
    """Item da lista que representa uma moeda no portfolio"""
    
    def __init__(self, symbol: str, name: str, amount: Decimal, **kwargs):
        super().__init__(**kwargs)
        card_style = get_card_style()
        
        # Configuração do card
        self.orientation = "horizontal"
        self.padding = card_style["padding"]
        self.spacing = card_style["spacing"]
        self.elevation = card_style["elevation"]
        self.radius = card_style["radius"]
        self.adaptive_height = True
        
        # Layout de informações
        info_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=STYLES["spacing"]["small"]
        )
        
        # Título com estilo subtitle
        title_style = get_font_style("subtitle")
        info_layout.add_widget(MDLabel(
            text=f"{name} ({symbol})",
            **title_style
        ))
        
        # Quantidade com estilo caption
        amount_style = get_font_style("caption")
        info_layout.add_widget(MDLabel(
            text=f"Quantidade: {float(amount):.8f}",  # Convertendo Decimal para float
            **amount_style
        ))
        
        self.add_widget(info_layout)