from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget  # Widget básico do Kivy
from kivy.animation import Animation  # Para animação de rotação
from kivy.properties import NumericProperty  # Para propriedade de rotação
from kivy.clock import Clock
from functools import partial
from typing import List, Optional
import asyncio
from ..config import STYLES, FONTS
from .base_screen import BaseScreen

# Widget personalizado para loading
class LoadingIndicator(Widget):
    angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = ("48dp", "48dp")
        self._anim = None
    
    def start(self):
        self._anim = Animation(angle=360, duration=1)
        self._anim.repeat = True
        self._anim.start(self)
    
    def stop(self):
        if self._anim:
            self._anim.cancel(self)

class PesquisaScreen(BaseScreen):
    """Tela de pesquisa de criptomoedas"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._search_trigger = Clock.create_trigger(self._do_search, .5)
        self._last_search: Optional[str] = None
        self._cache = {}

    def init_ui(self):
        """Inicializa componentes específicos desta tela"""
        self.add_title("Pesquisar Criptomoedas")
        
        # Container principal
        container = MDBoxLayout(
            orientation="vertical",
            adaptive_height=True,
            spacing=STYLES["spacing"]["default"]
        )
        
        # Campo de pesquisa atualizado
        self.search_field = MDTextField(
            hint_text="Pesquisar criptomoeda...",
            mode="filled",  # Alterado de 'rectangle' para 'filled'
            font_size="16sp",
            size_hint_y=None,
            height="48dp",
            on_text=self.on_search,
            pos_hint={"center_x": 0.5},
            size_hint_x=0.9  # 90% da largura do container
        )
        container.add_widget(self.search_field)
        
        # Indicador de carregamento
        self.loading_indicator = LoadingIndicator()
        self.loading_indicator.opacity = 0
        container.add_widget(self.loading_indicator)
        
        # Lista de resultados
        self.results_list = MDList(
            spacing=STYLES["spacing"]["small"],
            padding=STYLES["padding"]["small"]
        )
        container.add_widget(self.results_list)
        
        self.main_layout.add_widget(container)
    
    def on_search(self, instance, value: str):
        """Gatilho de pesquisa com debounce"""
        if len(value) < 2:
            self.update_results([])
            return
        
        self._last_search = value
        self._search_trigger()

    async def _do_search(self, *args):
        """Executa a pesquisa de forma assíncrona"""
        try:
            if not self._last_search:
                return

            # Verifica cache
            if self._last_search in self._cache:
                self.update_results(self._cache[self._last_search])
                return

            self.show_loading(True)
            
            # Chamada real à API (simulada nos testes)
            from src.screens.pesquisa_screen import search_crypto
            results = await search_crypto(self._last_search)
            
            # Atualiza cache e resultados
            self._cache[self._last_search] = results
            self.update_results(results)

        except Exception as e:
            print(f"Erro na pesquisa: {e}")
            self.show_error("Erro ao realizar pesquisa")
        finally:
            self.show_loading(False)

    def update_results(self, results):
        """Atualiza a lista de resultados"""
        self.results_list.clear_widgets()
        if not results:
            self.results_list.add_widget(
                MDLabel(
                    text="Nenhum resultado encontrado",
                    **FONTS["body"]
                )
            )
    
    def show_error(self, message: str):
        """Exibe mensagem de erro"""
        self.results_list.clear_widgets()
        self.results_list.add_widget(
            MDLabel(
                text=message,
                **{
                    **FONTS["body"],  # Spread do dicionário base
                    "theme_text_color": "Error"  # Sobrescreve o theme_text_color
                }
            )
        )

    def show_loading(self, is_loading: bool):
        """Controla visibilidade do loading"""
        if is_loading:
            self.loading_indicator.start()
            self.loading_indicator.opacity = 1
        else:
            self.loading_indicator.stop()
            self.loading_indicator.opacity = 0

async def search_crypto(query: str) -> List[dict]:
    # TODO: Implementar
    pass