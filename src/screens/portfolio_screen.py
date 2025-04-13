from typing import List
from decimal import Decimal
from kivy.logger import Logger
from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from src.config import STYLES, get_font_style, get_card_style, FONTS
from .base_screen import BaseScreen
from ..models.coin import Coin  # Assumindo que existe uma classe Coin

class PortfolioScreen(BaseScreen):
    """Tela de portfolio do usuário"""
    
    def __init__(self, portfolio_manager=None, **kwargs):
        self.portfolio = portfolio_manager  # Inicializa antes do super()
        super().__init__(**kwargs)
        self.coins_list = None
    
    def init_ui(self):
        """Inicializa componentes específicos desta tela"""
        if not self.portfolio:
            Logger.warning("Portfolio não inicializado")
            return

        self.add_title("Meu Portfolio")
        
        # Container principal
        self.coins_list = MDList(
            spacing=STYLES["spacing"]["default"],
            padding=STYLES["padding"]["default"]
        )
        self.main_layout.add_widget(self.coins_list)
        
        # Tenta atualizar a lista se o portfolio estiver disponível
        self.update_coins_list()
    
    def update_coins_list(self):
        """Atualiza lista de moedas do portfolio"""
        try:
            if not self.portfolio or not self.coins_list:
                return
                
            self.coins_list.clear_widgets()
            coins = self.portfolio.get_coins()
            
            if not coins:
                self.show_empty_message()
                return
                
            for coin in coins:
                self.add_coin_item(coin)
                
        except Exception as e:
            Logger.error(f"Erro ao atualizar lista: {str(e)}")
            self.show_error("Erro ao carregar portfolio")
    
    def show_empty_message(self):
        """Exibe mensagem quando não há moedas"""
        self.coins_list.add_widget(
            MDLabel(
                text="Nenhuma moeda adicionada",
                halign="center",
                theme_text_color="Secondary"
            )
        )

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