from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivy.uix.widget import Widget  # Widget básico do Kivy
from kivy.animation import Animation  # Para animação de rotação
from kivy.properties import NumericProperty  # Para propriedade de rotação
from kivy.clock import Clock
from functools import partial
from typing import List, Optional
import asyncio
from src.core.theme import STYLES, FONTS, apply_font_style
from src.api.crypto import search_crypto
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

class PesquisaScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._last_search = None
        self._cache = {}
        self._init_ui()
        
    def _init_ui(self):
        """Inicializa a interface"""
        self.layout = MDBoxLayout(
            orientation='vertical',
            spacing=STYLES["spacing"]["default"],
            padding=STYLES["padding"]["default"]
        )
        
        # Título - criando com configurações mínimas
        self.title = MDLabel(text="Pesquisar")
        
        # Aplicando estilo em duas etapas
        title_style = FONTS["title"]
        self.title.font_size = title_style["font_size"]  # Define tamanho primeiro
        apply_font_style(self.title, "title")  # Aplica outros estilos depois
        
        # Campo de pesquisa
        self.search_field = MDTextField(
            hint_text="Digite o nome da moeda",
            on_text_validate=self.on_search
        )
        
        self.layout.add_widget(self.title)
        self.layout.add_widget(self.search_field)
        
        # Lista de resultados
        self.results_list = MDBoxLayout(
            orientation='vertical',
            spacing=STYLES["spacing"]["small"]
        )
        self.layout.add_widget(self.results_list)
        
        # Indicador de loading
        self.loading_indicator = LoadingIndicator()
        self.loading_indicator.opacity = 0
        self.layout.add_widget(self.loading_indicator)
        
        self.add_widget(self.layout)

    def on_search(self, instance, value: str = None):
        """Callback quando texto é submetido"""
        if value is None and instance:
            value = instance.text
            
        if len(value) < 2:
            self.update_results([])
            return
            
        self._last_search = value
        asyncio.create_task(self._do_search())

    async def _do_search(self):
        """Executa pesquisa assíncrona"""
        query = self._last_search
        
        try:
            self.show_loading(True)
            
            # Verifica cache
            if query in self._cache:
                self.update_results(self._cache[query])
                return
                
            results = await search_crypto(query)
            self._cache[query] = results
            self.update_results(results)
            
        except Exception as e:
            self.show_error(f"Erro de API: {str(e)}")  # Mantém mensagem de erro consistente
        finally:
            self.show_loading(False)

    def update_results(self, results: List[dict]):
        """Atualiza lista de resultados"""
        self.results_list.clear_widgets()
        
        if not results:
            error_label = MDLabel(text="Nenhum resultado encontrado")
            apply_font_style(error_label, "body")
            self.results_list.add_widget(error_label)
            return

        for item in results:
            result_label = MDLabel(
                text=f"{item['symbol']} - {item['name']}"
            )
            apply_font_style(result_label, "body")
            self.results_list.add_widget(result_label)

    def show_loading(self, show: bool):
        """Controla visibilidade do loading"""
        if show:
            self.loading_indicator.opacity = 1
            self.loading_indicator.start()
        else:
            self.loading_indicator.opacity = 0
            self.loading_indicator.stop()

    def show_error(self, message: str):
        """
        Exibe mensagem de erro
        Args:
            message: Mensagem de erro para exibir
        """
        self.results_list.clear_widgets()
        error_label = MDLabel(text=f"Erro: {message}")
        apply_font_style(error_label, "body")
        error_label.theme_text_color = "Error"  # Sobrescreve o tema para erro
        self.results_list.add_widget(error_label)

async def search_crypto(query: str) -> List[dict]:
    # TODO: Implementar
    pass