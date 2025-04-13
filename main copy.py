import os
os.environ['KIVY_DEBUG'] = '1'
from kivy.logger import Logger
Logger.setLevel('DEBUG')

from kivy.lang import Builder
from kivymd.app import MDApp
from src.portfolio import Portfolio
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerItem,
    MDNavigationDrawerDivider
)
from src.screens.lista_screen import ListaScreen
from src.screens.portfolio_screen import PortfolioScreen
from src.screens.alertas_screen import AlertasScreen
from src.screens.pesquisa_screen import PesquisaScreen
from src.screens.noticias_screen import NoticiasScreen
from src.screens.conversor_screen import ConversorScreen
from pathlib import Path

KV = '''
MDScreen:
    md_bg_color: app.colors['background']
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    
                    MDTopAppBar:
                        title: "CryptoApp"
                        elevation: 2
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        specific_text_color: "white"
                        md_bg_color: app.colors['primary']
                    
                    ScreenManager:
                        id: content_manager

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)
            elevation: 4
            width: "240dp"
            anchor: "left"
            type: "modal"
            
            MDNavigationDrawerMenu:
                
                MDNavigationDrawerHeader:
                    title: "CryptoApp"
                    title_color: app.colors['text']
                    text: "Menu Principal"
                    spacing: "4dp"
                    padding: "12dp"
                
                MDNavigationDrawerItem:
                    icon: "view-list"
                    text: "Lista de Moedas"
                    on_press: 
                        app.change_screen("lista")
                        nav_drawer.set_state("close")
                
                MDNavigationDrawerItem:
                    icon: "wallet"
                    text: "Meu Portfolio"
                    on_press:
                        app.change_screen("portfolio")
                        nav_drawer.set_state("close")
                
                MDNavigationDrawerItem:
                    icon: "bell-outline"
                    text: "Alertas"
                    on_press:
                        app.change_screen("alertas")
                        nav_drawer.set_state("close")
                
                MDNavigationDrawerDivider:
                
                MDNavigationDrawerItem:
                    icon: "magnify"
                    text: "Pesquisar"
                    on_press:
                        app.change_screen("pesquisa")
                        nav_drawer.set_state("close")
                
                MDNavigationDrawerItem:
                    icon: "newspaper-variant-outline"
                    text: "Notícias"
                    on_press:
                        app.change_screen("noticias")
                        nav_drawer.set_state("close")
                
                MDNavigationDrawerItem:
                    icon: "currency-usd"
                    text: "Conversor"
                    on_press:
                        app.change_screen("conversor")
                        nav_drawer.set_state("close")
'''

class CryptoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.portfolio = None
        
        # Configuração do tema
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.accent_palette = "Orange"
        self.theme_cls.material_style = "M3"
        
        self._screen_manager = None
        self.title = "CryptoApp"
        self._kv_loaded = False
        
        # Cores personalizadas usando RGB normalizado (0-1)
        self.colors = {
            'primary': [0.26, 0.36, 0.85, 1],    # Indigo
            'accent': [1, 0.65, 0, 1],           # Orange
            'background': [0.98, 0.98, 0.98, 1], # Quase branco
            'surface': [1, 1, 1, 1],             # Branco
            'text': [0.1, 0.1, 0.1, 1]          # Texto escuro
        }

    def build(self):
        # Configura tamanho padrão para mobile
        from kivy.core.window import Window
        Window.size = (400, 700)  # Tamanho típico de smartphone
        
        try:
            # Inicializa o portfolio primeiro
            if not self.portfolio:
                self.portfolio = Portfolio()
                Logger.info("Portfolio inicializado")
            
            # Carrega KV apenas uma vez
            if not self._kv_loaded:
                root = Builder.load_string(KV)
                self._kv_loaded = True
                
                # Configura gerenciador de telas
                self._screen_manager = root.ids.content_manager
                
                # Remove telas existentes para evitar duplicação
                self._screen_manager.clear_widgets()
                
                # Adiciona telas programaticamente com suas dependências
                screens = {
                    'lista': ListaScreen(),  # CoinGeckoService já é inicializado no construtor
                    'portfolio': PortfolioScreen(portfolio_manager=self.portfolio),
                    'alertas': AlertasScreen(),
                    'pesquisa': PesquisaScreen(),
                    'noticias': NoticiasScreen(),
                    'conversor': ConversorScreen()
                }
                
                for name, screen in screens.items():
                    Logger.debug(f"Adicionando tela: {name}")
                    screen.name = name
                    self._screen_manager.add_widget(screen)
                
                # Define tela inicial
                self._screen_manager.current = 'lista'
                Logger.info("Aplicação inicializada com sucesso")
                
                return root
            
        except Exception as e:
            Logger.error(f"Erro na inicialização: {str(e)}")
            import traceback
            Logger.error(traceback.format_exc())
            return None

    def change_screen(self, screen_name):
        """Muda para a tela especificada com tratamento de erro melhorado"""
        try:
            if not self._screen_manager:
                Logger.error("ScreenManager não inicializado")
                return
                
            if screen_name not in self._screen_manager.screen_names:
                Logger.error(f"Tela '{screen_name}' não encontrada")
                return
                
            self._screen_manager.current = screen_name
            Logger.info(f"Tela alterada para: {screen_name}")
            
        except Exception as e:
            Logger.error(f"Erro ao mudar tela: {str(e)}")

if __name__ == '__main__':
    CryptoApp().run()