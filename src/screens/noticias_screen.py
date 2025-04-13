from kivymd.uix.list import MDList
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from ..core.theme import STYLES, FONTS
from .base_screen import BaseScreen

# Base para todos os cards
class BaseCard(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = STYLES["padding"]["default"]
        self.spacing = STYLES["spacing"]["small"]
        self.radius = STYLES["radius"]["default"]
        self.elevation = 1

class NoticiaCard(BaseCard):
    """Card personalizado para notícias"""
    def __init__(self, titulo, descricao, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        self.height = "120dp"
        
        # Layout para informações
        info_layout = MDBoxLayout(
            orientation="vertical",
            spacing=STYLES["spacing"]["small"]
        )
        
        # Título com estilo correto
        info_layout.add_widget(MDLabel(
            text=titulo,
            **FONTS["title"]  # Usando configuração completa do título
        ))
        
        # Descrição com estilo correto
        info_layout.add_widget(MDLabel(
            text=descricao,
            **FONTS["body"]  # Usando configuração completa do corpo
        ))
        
        self.add_widget(info_layout)

class NoticiasScreen(BaseScreen):
    """Tela de notícias sobre criptomoedas"""
    
    def init_ui(self):
        """Inicializa componentes específicos desta tela"""
        self.add_title("Últimas Notícias")
        
        # Lista de notícias
        self.news_list = MDList(
            spacing=STYLES["spacing"]["small"],
            padding=STYLES["padding"]["small"]
        )
        self.main_layout.add_widget(self.news_list)
        
        # Carregar notícias iniciais
        self.atualizar_noticias()
    
    def atualizar_noticias(self):
        """Atualiza a lista de notícias"""
        self.news_list.clear_widgets()
        
        # Exemplo de notícias (substituir por dados reais)
        noticias = [
            {
                "titulo": "Bitcoin atinge nova máxima",
                "descricao": "A principal criptomoeda atingiu novo recorde histórico..."
            },
            {
                "titulo": "Ethereum 2.0 se aproxima",
                "descricao": "Atualização promete melhorar escalabilidade da rede..."
            }
        ]
        
        for noticia in noticias:
            self.news_list.add_widget(
                NoticiaCard(
                    titulo=noticia["titulo"],
                    descricao=noticia["descricao"]
                )
            )