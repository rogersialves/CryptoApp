from kivy.app import App
from src.ui import CryptoControlUI
from src.portfolio import Portfolio

class CryptoControlApp(App):
    def build(self):
        self.title = 'CryptoApp'
        self.portfolio = Portfolio()
        return CryptoControlUI(portfolio=self.portfolio)

if __name__ == '__main__':
    CryptoControlApp().run()