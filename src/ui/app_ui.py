from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from decimal import Decimal, InvalidOperation
from dataclasses import dataclass
from typing import List, Dict
from ..portfolio import Portfolio

@dataclass
class CoinData:
    symbol: str
    amount: Decimal
    avg_price: Decimal

class CryptoAppUI(App):
    def __init__(self, portfolio: Portfolio = None, **kwargs):
        super().__init__(**kwargs)
        self.portfolio = portfolio or Portfolio()
        self._init_ui()

    def _init_ui(self):
        """Inicializa a interface"""
        self.main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Campos de entrada básicos
        self.symbol_input = TextInput(
            multiline=False,
            text=''
        )
        
        self.amount_input = TextInput(
            multiline=False,
            text=''
        )
        
        self.price_input = TextInput(
            multiline=False,
            text=''
        )
        
        # Labels e botões
        self.add_button = Button(text='Adicionar')
        self.add_button.bind(on_press=self.add_transaction)
        
        self.status_label = Label(text='')
        self.holdings_label = Label(text='Portfolio vazio')
        
        # Adiciona widgets ao layout
        widgets = [
            self.symbol_input,
            self.amount_input,
            self.price_input,
            self.add_button,
            self.status_label,
            self.holdings_label
        ]
        
        for widget in widgets:
            self.main_layout.add_widget(widget)
            
        return self.main_layout

    def add_transaction(self, instance):
        """Adiciona uma nova transação"""
        try:
            symbol = self.symbol_input.text.strip().upper()
            if not symbol:
                raise ValueError("Símbolo não pode estar vazio")
                
            amount = Decimal(self.amount_input.text)
            price = Decimal(self.price_input.text)
            
            self.portfolio.add_transaction(symbol, amount, price)
            self.update_view()
            self.clear_inputs()
            self.status_label.text = "Transação adicionada com sucesso"
            
        except (ValueError, InvalidOperation) as e:
            self.status_label.text = f"Erro: {str(e)}"

    def parse_coin_data(self, coin_dict: Dict) -> CoinData:
        """Converte dicionário em CoinData"""
        return CoinData(
            symbol=str(coin_dict["symbol"]),
            amount=Decimal(str(coin_dict["amount"])),
            avg_price=Decimal(str(coin_dict["avg_price"]))
        )

    def update_view(self):
        """Atualiza visualização do portfolio"""
        coins = self.portfolio.get_coins()
        if not coins:
            self.holdings_label.text = "Portfolio vazio"
            return

        holdings_text = []
        for coin_dict in coins:
            coin = self.parse_coin_data(coin_dict)
            holdings_text.append(
                f"{coin.symbol}: {coin.amount} @ {coin.avg_price}"
            )
        self.holdings_label.text = "\n".join(holdings_text)
    
    def clear_inputs(self):
        """Limpa os campos de entrada"""
        self.symbol_input.text = ""
        self.amount_input.text = ""
        self.price_input.text = ""