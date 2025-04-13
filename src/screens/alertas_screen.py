from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from .base_screen import BaseScreen
from src.core.theme import STYLES, get_font_style, get_card_style  # Corrigido o caminho de importação


class AlertListItem(MDCard):
    """Item personalizado para lista de alertas"""
    def __init__(self, symbol, price_target, condition, **kwargs):
        super().__init__(**kwargs)
        card_style = get_card_style()
        
        self.orientation = "horizontal"
        self.padding = card_style["padding"]
        self.spacing = card_style["spacing"]
        self.elevation = card_style["elevation"]
        self.radius = card_style["radius"]
        self.adaptive_height = True
        
        info_layout = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=STYLES["spacing"]["small"]
        )
        
        # Título do alerta com estilo padronizado
        title_style = get_font_style("subtitle")
        info_layout.add_widget(MDLabel(
            text=f"{symbol}",
            **title_style
        ))
        
        # Condição do alerta com estilo padronizado
        caption_style = get_font_style("caption")
        info_layout.add_widget(MDLabel(
            text=f"{condition} R$ {price_target:.2f}",
            **caption_style
        ))
        
        self.add_widget(info_layout)


class AlertasScreen(BaseScreen):
    """Tela de alertas de preço"""
    
    def init_ui(self):
        """Inicializa componentes específicos desta tela"""
        self.add_title("Alertas de Preço")
        
        self.alerts_list = MDList(
            spacing=STYLES["spacing"]["small"],
            padding=STYLES["padding"]["small"]
        )
        self.main_layout.add_widget(self.alerts_list)
        self.update_alerts_list()
    
    def update_alerts_list(self):
        """Atualiza a lista de alertas"""
        self.alerts_list.clear_widgets()
        
        # Exemplo de alertas (substituir por dados reais)
        alerts = [
            {
                "symbol": "BTC",       # Símbolo da moeda
                "price_target": 250000.00, # Preço alvo
                "condition": "Acima de"    # Condição (ex: "Acima de", "Abaixo de")
            },
            {
                "symbol": "ETH",       # Símbolo da moeda
                "price_target": 15000.00,  # Preço alvo
                "condition": "Abaixo de"   # Condição (ex: "Acima de", "Abaixo de")
            }
        ]
        
        for alert in alerts:
            self.alerts_list.add_widget(
                AlertListItem(
                    symbol=alert["symbol"],
                    price_target=alert["price_target"],
                    condition=alert["condition"]
                )
            )
    
    def show_add_alert(self, *args):
        """Exibe diálogo para adicionar alerta"""
        print("Adicionar novo alerta")