"""Configurações de tema e estilo da interface"""
from typing import Dict, Any
from kivy.logger import Logger
from kivymd.uix.label import MDLabel
from kivymd.font_definitions import theme_font_styles

FONTS = {
    "display": {
        "font_name": "Roboto",
        "font_style": "H4",  # Estilos KivyMD válidos
        "theme_text_color": "Primary",
        "font_size": 34  # Valor numérico sem 'sp'
    },
    "title": {
        "font_name": "Roboto",
        "font_style": "H5",  # Mudado de H6 para H5 que é garantido existir
        "theme_text_color": "Primary", 
        "font_size": 20
    },
    "body": {
        "font_name": "Roboto",
        "font_style": "Body1",
        "theme_text_color": "Primary",
        "font_size": 16
    },
    "subtitle": {
        "font_name": "Roboto",
        "font_style": "Subtitle1",
        "theme_text_color": "Secondary",
        "font_size": 14
    },
    "caption": {
        "font_name": "Roboto",
        "font_style": "Caption",
        "theme_text_color": "Secondary",
        "font_size": 12
    }
}

# Estilos de layout
STYLES = {
    "spacing": {
        "default": "8dp",
        "small": "4dp",
        "large": "16dp"
    },
    "padding": {
        "default": ["16dp", "16dp", "16dp", "16dp"],
        "small": ["8dp", "8dp", "8dp", "8dp"],
        "large": ["24dp", "24dp", "24dp", "24dp"]
    }
}

# Adicionando configuração de cards
CARD_STYLE = {
    "elevation": 1,
    "radius": [8],
    "padding": STYLES["padding"]["default"],
    "spacing": STYLES["spacing"]["default"],
    "md_bg_color": [1, 1, 1, 1],  # Branco
    "shadow_softness": 2,
    "shadow_offset": (0, 1)
}

def get_font_style(style_name: str) -> Dict[str, Any]:
    """Retorna configuração de estilo de fonte com fallback"""
    return FONTS.get(style_name, FONTS["body"])

def get_card_style(style_name: str = "default") -> Dict[str, Any]:
    """
    Retorna configuração de estilo para cards
    Args:
        style_name: Nome do estilo (default, compact, elevated)
    Returns:
        Dict com configurações do card
    """
    # Estilos personalizados de cards
    card_styles = {
        "default": CARD_STYLE,
        "compact": {
            **CARD_STYLE,
            "padding": STYLES["padding"]["small"],
            "spacing": STYLES["spacing"]["small"]
        },
        "elevated": {
            **CARD_STYLE,
            "elevation": 3,
            "shadow_softness": 4
        }
    }
    return card_styles.get(style_name, CARD_STYLE)

def apply_font_style(widget: MDLabel, style_name: str = "body") -> None:
    """
    Aplica estilo de fonte a um widget de forma segura
    Args:
        widget: Widget MDLabel para aplicar o estilo
        style_name: Nome do estilo a ser aplicado
    """
    if not isinstance(widget, MDLabel):
        raise ValueError("Widget deve ser uma instância de MDLabel")
    
    style = FONTS.get(style_name, FONTS["body"])
    
    # Aplica propriedades na ordem específica
    widget.font_name = style["font_name"]
    widget.theme_text_color = style["theme_text_color"]
    
    # Define font_style antes do font_size para evitar sobrescrita
    if style["font_style"] in theme_font_styles:
        widget.font_style = style["font_style"]
    
    # Define font_size por último para garantir que não seja sobrescrito
    widget.font_size = style["font_size"]

def create_themed_label(text: str, style_name: str = "body") -> MDLabel:
    """Cria um label com estilo do tema de forma segura"""
    style = FONTS.get(style_name, FONTS["body"])
    
    # Cria label com configurações básicas primeiro
    label = MDLabel(
        text=text,
        font_name=style["font_name"],
        font_size=style["font_size"],
        theme_text_color=style["theme_text_color"]
    )
    
    # Define o estilo após a criação do label
    if style["font_style"] in theme_font_styles:
        label.font_style = style["font_style"]
    
    return label