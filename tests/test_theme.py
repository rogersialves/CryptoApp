import pytest
from pathlib import Path
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles
from kivy.core.window import Window
from src.core.theme import get_font_style, get_card_style, FONTS, STYLES

# Definindo o caminho base do projeto
PROJECT_ROOT = Path(__file__).parent.parent

@pytest.fixture(scope="session")
def kivy_app():
    """Fixture que fornece uma instância do app para os testes"""
    class TestApp(MDApp):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.theme_cls.theme_style = "Light"
            # Converte Path para string antes de passar para load_all_kv_files
            kv_path = str(PROJECT_ROOT / "src")
            self.load_all_kv_files(kv_path)
        
        def build(self):
            screen = MDScreen()
            return screen
    
    app = TestApp()
    app.build()  # Cria a tela root
    return app

@pytest.fixture
def font_styles():
    """Fixture com estilos de fonte padrão"""
    return ["display", "title", "subtitle", "body", "caption"]

def _validate_font_style(style_name: str, font_config: dict) -> bool:
    """Helper para validar configuração de estilo de fonte"""
    required_props = ["font_style", "theme_text_color", "font_size"]
    return all(prop in font_config for prop in required_props)

def test_font_styles_exist():
    """Testa se os estilos de fonte contém as propriedades necessárias"""
    required_props = {'font_name', 'font_style', 'theme_text_color', 'font_size'}
    
    for style_name, style in FONTS.items():
        for prop in required_props:
            assert prop in style, f"Propriedade {prop} não encontrada em {style_name}"

def test_font_styles_valid(kivy_app):
    """Testa se os estilos de fonte são válidos"""
    for style_name, font_style in FONTS.items():
        try:
            # Cria label sem font_style inicialmente
            label = MDLabel(
                text="Test",
                font_name=font_style["font_name"],
                theme_text_color=font_style["theme_text_color"],
                font_size=font_style["font_size"]  # Define font_size diretamente
            )
            
            # Define font_style após criação
            if font_style["font_style"] in theme_font_styles:
                label.font_style = font_style["font_style"]
            
            assert isinstance(label, MDLabel)
            
        except Exception as e:
            pytest.fail(f"Falha ao criar label com estilo {style_name}: {str(e)}")

def test_font_style_fallback():
    """Testa fallback de estilo"""
    style = get_font_style("invalid_style")
    assert style == FONTS["body"]

def test_card_style():
    """Testa se o estilo de card tem propriedades necessárias"""
    card_style = get_card_style()
    required_props = ["padding", "elevation", "radius", "md_bg_color"]
    for prop in required_props:
        assert prop in card_style

# Testes adicionais para validar valores específicos
def test_font_sizes(font_styles):
    """Testa se todos os estilos de fonte têm tamanhos válidos"""
    for style_name in font_styles:
        font_config = FONTS[style_name]
        assert "font_size" in font_config, f"Estilo {style_name} não tem font_size"
        assert isinstance(font_config["font_size"], (int, float)), f"font_size deve ser numérico"
        assert font_config["font_size"] > 0, f"font_size deve ser positivo"

def test_theme_colors(font_styles):
    """Testa se as cores do tema são válidas"""
    valid_colors = ["Primary", "Secondary", "Error", "ContrastParentBackground"]
    for style_name in font_styles:
        font_config = FONTS[style_name]
        assert font_config["theme_text_color"] in valid_colors