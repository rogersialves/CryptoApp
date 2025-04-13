from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from src.screens.base_screen import BaseScreen

class ConversorScreen(BaseScreen):
    def init_ui(self):
        # Layout principal
        content_layout = MDBoxLayout(
            orientation="vertical",
            spacing="16dp",
            padding=["16dp", "16dp", "16dp", "16dp"]
        )

        # Campo de entrada
        self.amount_input = MDTextField(
            hint_text="Digite o valor",
            mode="outlined",
            size_hint_y=None,
            height="48dp",
            input_type="number",
            input_filter="float"
        )

        # Campos de moeda
        self.from_currency = MDTextField(
            hint_text="De (ex: BTC)",
            mode="outlined",
            size_hint_y=None,
            height="48dp"
        )

        self.to_currency = MDTextField(
            hint_text="Para (ex: USD)",
            mode="outlined",
            size_hint_y=None,
            height="48dp"
        )

        # Container para o botão
        button_container = MDBoxLayout(
            size_hint_y=None,
            height="48dp",
            padding=[0, 8, 0, 8]
        )

        # Botão de conversão com propriedades suportadas
        convert_button = MDButton(
            style="filled",
            _button_text="Converter",
            size_hint_x=1,
            size_hint_y=None,
            height="48dp",
            md_bg_color=self.theme_cls.primaryColor,
            on_release=self.convert
        )

        button_container.add_widget(convert_button)

        # Resultado da conversão
        self.result_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )

        # Adiciona os widgets ao layout
        content_layout.add_widget(self.amount_input)
        content_layout.add_widget(self.from_currency)
        content_layout.add_widget(self.to_currency)
        content_layout.add_widget(button_container)
        content_layout.add_widget(self.result_label)
        self.main_layout.add_widget(content_layout)

    def convert(self, *args):
        """Realiza a conversão entre as moedas"""
        try:
            # Obtém os valores dos campos
            amount = float(self.amount_input.text or "0")
            from_curr = self.from_currency.text.upper()
            to_curr = self.to_currency.text.upper()
            
            # Validação básica
            if not all([amount, from_curr, to_curr]):
                self.result_label.text = "Preencha todos os campos"
                return
            
            # TODO: Implementar lógica de conversão real
            # Por enquanto apenas mostra os valores informados
            result = f"{amount} {from_curr} = ? {to_curr}"
            self.result_label.text = result
            
        except ValueError:
            self.result_label.text = "Digite um valor válido"
        except Exception as e:
            self.result_label.text = f"Erro: {str(e)}"