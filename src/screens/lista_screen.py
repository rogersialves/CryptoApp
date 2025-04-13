from kivymd.uix.card import MDCard
from kivy.logger import Logger
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDIconButton
from kivymd.uix.screen import MDScreen
from src.core.theme import STYLES  # Atualizado o import
from src.screens.base_screen import BaseScreen
from src.services.coingecko_service import CoinGeckoService

class CryptoListItem(MDBoxLayout):
    def __init__(self, coin_data, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = "85dp"  # Aumentado um pouco para melhor espaçamento
        self.padding = [8, 4]
        
        # Card principal
        content = MDCard(
            orientation="vertical",
            size_hint=(1, None),
            height="77dp",
            padding="8dp",  # Reduzido padding
            radius=[12],
            elevation=0,
            md_bg_color=[0.95, 0.95, 0.95, 1]
        )
        
        # Layout principal
        main_layout = MDBoxLayout(
            orientation="horizontal",
            spacing="4dp"  # Reduzido espaçamento
        )
        
        # Coluna esquerda (nome e símbolo)
        left_col = MDBoxLayout(
            orientation="vertical",
            size_hint_x=0.6,  # Aumentado para dar mais espaço ao nome
            spacing="2dp"
        )
        
        # Nome da moeda
        left_col.add_widget(MDLabel(
            text=coin_data["name"],
            font_size="15sp",  # Reduzido
            bold=True,
            theme_text_color="Primary"
        ))
        
        # Símbolo da moeda
        left_col.add_widget(MDLabel(
            text=coin_data["symbol"].upper(),
            font_size="13sp",  # Reduzido
            theme_text_color="Secondary"
        ))
        
        main_layout.add_widget(left_col)
        
        # Coluna direita (preço e variação)
        right_col = MDBoxLayout(
            orientation="vertical",
            size_hint_x=0.4,  # Reduzido para equilibrar com a esquerda
            spacing="2dp"
        )
        
        # Preço
        price_label = MDLabel(
            text=f"${coin_data['current_price']:,.2f}",
            font_size="14sp",  # Reduzido
            bold=True,
            halign="right",
            theme_text_color="Primary"
        )
        right_col.add_widget(price_label)
        
        # Variação 24h
        price_change = coin_data.get('price_change_percentage_24h', 0)
        change_color = [0, 0.7, 0, 1] if price_change >= 0 else [0.7, 0, 0, 1]
        
        change_label = MDLabel(
            text=f"{'+' if price_change >= 0 else ''}{price_change:.2f}%",
            font_size="13sp",  # Reduzido
            halign="right",
            theme_text_color="Custom",
            text_color=change_color
        )
        right_col.add_widget(change_label)
        
        main_layout.add_widget(right_col)
        content.add_widget(main_layout)
        
        # Volume 24h
        volume_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="18dp"  # Reduzido
        )
        
        volume_layout.add_widget(MDLabel(
            text=f"Vol 24h: ${coin_data['total_volume']:,.0f}",
            font_size="11sp",  # Reduzido
            theme_text_color="Secondary"
        ))
        
        content.add_widget(volume_layout)
        self.add_widget(content)

class ListaScreen(BaseScreen):
    def __init__(self, **kwargs):
        self.coingecko = CoinGeckoService()  # Inicializa antes do super()
        super().__init__(**kwargs)

    def init_ui(self):
        # Container principal com padding lateral apenas
        content_layout = MDBoxLayout(
            orientation="vertical",
            spacing="4dp",
            padding=[16, 0, 16, 0]  # [esquerda, topo, direita, baixo]
        )
        
        # ScrollView e lista
        scroll = ScrollView(
            do_scroll_x=False,
            size_hint=(1, 1)
        )
        
        self.crypto_list = MDList(
            spacing="4dp",
            padding=[0, 0, 0, 0]
        )
        
        # Carrega e monta a hierarquia
        self.load_crypto_data()
        scroll.add_widget(self.crypto_list)
        content_layout.add_widget(scroll)
        self.main_layout.add_widget(content_layout)
    
    def load_crypto_data(self):
        """Carrega dados das criptomoedas do CoinGecko"""
        try:
            coins = self.coingecko.get_top_coins()
            for coin in coins:
                item = CryptoListItem(coin)
                self.crypto_list.add_widget(item)
        except Exception as e:
            Logger.error(f"Erro ao carregar dados: {str(e)}")