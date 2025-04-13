from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from ..core.theme import STYLES, FONTS

class BaseScreen(MDScreen):
    """Classe base para todas as telas do app"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Layout principal que contém todo o conteúdo da tela
        self.main_layout = MDBoxLayout(
            orientation="vertical",
            spacing="0dp",  # Removido espaçamento
            padding=[0, 0, 0, 0]  # Removido padding
        )
        self.add_widget(self.main_layout)
        self.init_ui()
    
    def on_enter(self):
        """Chamado quando a tela é exibida"""
        if not self.initialized:
            print(f"Inicializando UI da tela: {self.name}")
            self.init_ui()
            self.initialized = True
    
    def add_title(self, text):
        title = MDLabel(
            text=text,
            # Removendo font_style_name que não é uma propriedade válida
            font_style="H5",  # Usando font_style ao invés de font_style_name
            halign="center",
            size_hint_y=None,
            height=dp(50)
        )
        self.add_widget(title)
    
    def init_ui(self):
        """Método a ser sobrescrito pelas classes filhas"""
        raise NotImplementedError