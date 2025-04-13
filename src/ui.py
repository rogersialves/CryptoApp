from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from decimal import Decimal, InvalidOperation
from .portfolio import Portfolio

class CryptoControlUI(BoxLayout):
    def __init__(self, portfolio=None, **kwargs):
        super().__init__(**kwargs)
        self.portfolio = portfolio
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        
        # Campos de entrada
        self.symbol_input = TextInput(hint_text='Símbolo (ex: BTC)')
        self.amount_input = TextInput(hint_text='Quantidade')
        self.price_input = TextInput(hint_text='Preço')
        
        # Labels
        self.status_label = Label(text='')
        self.holdings_label = Label(text='')
        
        # Botão
        self.add_button = Button(
            text='Adicionar Transação',
            on_press=self.add_transaction
        )
        
        # Adiciona widgets
        self.add_widget(self.symbol_input)
        self.add_widget(self.amount_input)
        self.add_widget(self.price_input)
        self.add_widget(self.add_button)
        self.add_widget(self.status_label)
        self.add_widget(self.holdings_label)
        
        # Atualiza view
        self.update_view()
        
        # Agenda primeira atualização
        Clock.schedule_once(lambda dt: self.update_view())
    
    def add_transaction(self, instance):
        """Adiciona uma nova transação"""
        try:
            symbol = self.symbol_input.text.strip()
            amount = Decimal(self.amount_input.text)
            price = Decimal(self.price_input.text)
            
            if not symbol:
                raise ValueError("Símbolo não pode estar vazio")
            
            self.portfolio.add_transaction(symbol, amount, price)
            self.status_label.text = 'Transação adicionada com sucesso'
            
            # Agenda atualização da view para o próximo frame
            Clock.schedule_once(lambda dt: self.update_view())
            
        except (ValueError, InvalidOperation) as e:
            self.status_label.text = f'Erro: {str(e)}'
    
    def update_view(self, *args):
        """Atualiza a visualização do portfolio"""
        if not self.portfolio:
            return
            
        summary = self.portfolio.get_portfolio_summary()
        holdings_text = []
        
        for symbol, data in summary['holdings'].items():
            holdings_text.append(
                f"{symbol}: {data['amount']} @ {data['avg_price']}"
            )
        
        self.holdings_label.text = '\n'.join(holdings_text) if holdings_text else "Nenhuma transação"

    def clear_inputs(self):
        """Limpa todos os campos de entrada"""
        self.symbol_input.text = ""
        self.amount_input.text = ""
        self.price_input.text = ""

    def get_holdings_text(self):
        """Retorna o texto atual dos holdings"""
        return self.holdings_label.text

    def set_status(self, message):
        """Define uma mensagem de status"""
        self.status_label.text = message