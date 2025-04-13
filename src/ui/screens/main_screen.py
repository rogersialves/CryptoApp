from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from src.core.theme import FONTS, STYLES, apply_font_style

class MainScreen(MDScreen):
    """Tela principal do aplicativo"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._init_ui()
        
    def _init_ui(self):
        """Inicializa componentes da UI"""
        self.layout = MDBoxLayout(
            orientation='vertical',
            spacing=STYLES["spacing"]["default"],
            padding=STYLES["padding"]["default"]
        )
        
        # Campos de entrada
        self.amount_input = MDTextField(
            hint_text="Quantidade",
            helper_text="Digite um número válido",
            helper_text_mode="on_error"
        )
        
        # Label de erro
        self.error_label = MDLabel(text="")
        apply_font_style(self.error_label, "body")
        self.error_label.theme_text_color = "Error"
        
        # Adiciona widgets
        self.layout.add_widget(self.amount_input)
        self.layout.add_widget(self.error_label)
        self.add_widget(self.layout)
    
    async def validate_amount(self):
        """Valida o valor inserido no campo quantidade"""
        try:
            amount = float(self.amount_input.text)
            if amount <= 0:
                raise ValueError()
            self.error_label.text = ""
            return True
        except ValueError:
            self.error_label.text = "Quantidade inválida"
            return False