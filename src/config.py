from typing import Dict, Any

"""Configurações globais do aplicativo"""

# Configurações de tema
THEME = {
    "primary_palette": "Orange",
    "accent_palette": "Blue",
    "theme_style": "Light"
}

# Configurações de espaçamento
STYLES = {
    "padding": {
        "default": "16dp",
        "small": "8dp",
        "large": "24dp"
    },
    "spacing": {
        "default": "16dp",
        "small": "8dp",
        "large": "24dp"
    },
    "radius": {
        "default": "8dp",
        "small": "4dp",
        "large": "16dp"
    }
}

# Estilos de fonte atualizados para Material Design 3
FONTS = {
    "display": {
        "font_style": "Display",
        "font_size": "34sp",
        "theme_text_color": "Primary",
        "role": "large",
        "halign": "center"
    },
    "title": {
        "font_style": "Title",
        "font_size": "20sp",
        "theme_text_color": "Primary",
        "role": "medium",
        "halign": "left"
    },
    "body": {
        "font_style": "Body",
        "font_size": "16sp",
        "theme_text_color": "Secondary",
        "role": "small",
        "halign": "left"
    }
}

# Configurações de cards
CARDS = {
    "default": {
        "elevation": 1,
        "radius": "8dp",
        "padding": "16dp",
        "spacing": "8dp"
    }
}

def get_font_style(style_type: str) -> Dict[str, Any]:
    """Retorna configurações de fonte"""
    return FONTS.get(style_type, FONTS["body"])

def get_card_style(style_type: str = "default") -> Dict[str, Any]:
    """Retorna configurações de card"""
    return CARDS.get(style_type, CARDS["default"])