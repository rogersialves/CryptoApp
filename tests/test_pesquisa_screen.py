import pytest
from unittest.mock import Mock, patch
import asyncio  # Adicionando importação necessária
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from src.screens.pesquisa_screen import PesquisaScreen

@pytest.fixture
def mock_fonts():
    """Fixture para simular configurações de fonte"""
    return {
        "display": {
            "font_style": "Display",
            "font_size": "34sp",
            "theme_text_color": "Primary",
            "role": "large",
            "halign": "center"
        },
        "body": {
            "font_style": "Body",
            "font_size": "16sp",
            "theme_text_color": "Secondary",
            "role": "small",
            "halign": "left"
        }
    }

@pytest.fixture
def mock_styles():
    """Fixture para simular configurações de estilo"""
    return {
        "spacing": {"default": "16dp", "small": "8dp"},
        "padding": {"default": "16dp", "small": "8dp"}
    }

@pytest.fixture
def pesquisa_screen(mock_app, mock_fonts, mock_styles, monkeypatch):
    """Fixture que cria uma instância da tela de pesquisa"""
    from src import config
    monkeypatch.setattr(config, 'FONTS', mock_fonts)
    monkeypatch.setattr(config, 'STYLES', mock_styles)
    
    screen = PesquisaScreen()
    screen.init_ui()
    return screen

def test_init_screen(pesquisa_screen):
    """Testa inicialização básica da tela"""
    assert pesquisa_screen.search_field is not None
    assert pesquisa_screen.search_field.hint_text == "Pesquisar criptomoeda..."
    assert pesquisa_screen.results_list is not None
    assert pesquisa_screen._cache == {}
    assert pesquisa_screen.loading_indicator is not None
    assert pesquisa_screen.loading_indicator.opacity == 0

def test_init_pesquisa_screen(pesquisa_screen):
    """Testa se a tela é inicializada corretamente"""
    assert isinstance(pesquisa_screen, MDScreen)
    assert pesquisa_screen._last_search is None
    assert isinstance(pesquisa_screen._cache, dict)

@pytest.mark.asyncio
async def test_search_validation(pesquisa_screen):
    """Testa validação do texto de pesquisa"""
    # Mock do método update_results
    pesquisa_screen.update_results = Mock()
    
    # Testa texto muito curto
    pesquisa_screen.on_search(None, "a")
    pesquisa_screen.update_results.assert_called_with([])
    
    # Testa texto válido
    pesquisa_screen.on_search(None, "bitcoin")
    assert pesquisa_screen._last_search == "bitcoin"

@pytest.mark.asyncio
async def test_search_flow(pesquisa_screen):
    """Testa o fluxo completo de pesquisa"""
    mock_results = [{"symbol": "BTC", "name": "Bitcoin"}]
    
    # Mock da função de pesquisa e do método _do_search
    with patch('src.screens.pesquisa_screen.search_crypto', return_value=mock_results):
        # Simula a pesquisa
        pesquisa_screen.on_search(None, "bitcoin")
        
        # Força execução do _do_search diretamente já que o trigger pode não executar nos testes
        await pesquisa_screen._do_search()
        
        # Verifica se o cache foi atualizado
        assert "bitcoin" in pesquisa_screen._cache
        assert pesquisa_screen._cache["bitcoin"] == mock_results

@pytest.mark.asyncio
async def test_empty_results(pesquisa_screen):
    """Testa exibição de resultados vazios"""
    pesquisa_screen.update_results([])
    
    # Deve haver apenas um widget (mensagem de sem resultados)
    assert len(pesquisa_screen.results_list.children) == 1
    label = pesquisa_screen.results_list.children[0]
    assert isinstance(label, MDLabel)
    assert "Nenhum resultado encontrado" in label.text

@pytest.mark.asyncio
async def test_error_handling(pesquisa_screen):
    """Testa tratamento de erros"""
    error_msg = "Erro de conexão"
    pesquisa_screen.show_error(error_msg)
    
    # Verifica mensagem de erro
    label = pesquisa_screen.results_list.children[0]
    assert isinstance(label, MDLabel)
    assert error_msg in label.text
    assert label.theme_text_color == "Error"

@pytest.mark.asyncio
async def test_do_search_cache(pesquisa_screen):
    """Testa o funcionamento do cache na pesquisa"""
    # Prepara dados mockados
    mock_results = [{"symbol": "BTC", "name": "Bitcoin"}]
    pesquisa_screen._cache = {"bitcoin": mock_results}
    pesquisa_screen.update_results = Mock()
    
    # Simula pesquisa com termo cacheado
    pesquisa_screen._last_search = "bitcoin"
    await pesquisa_screen._do_search()
    
    # Verifica se retornou do cache
    pesquisa_screen.update_results.assert_called_with(mock_results)

@pytest.mark.asyncio
async def test_do_search_error(pesquisa_screen):
    """Testa o tratamento de erro na pesquisa"""
    # Mock para simular erro
    pesquisa_screen.show_error = Mock()
    pesquisa_screen._last_search = "error"
    
    with patch('asyncio.sleep', side_effect=Exception("Erro de API")):
        await pesquisa_screen._do_search()
        
    pesquisa_screen.show_error.assert_called_with("Erro ao realizar pesquisa")

def test_loading_indicators(pesquisa_screen):
    """Testa indicadores de carregamento"""
    # Testa início do loading
    pesquisa_screen.show_loading(True)
    assert pesquisa_screen.loading_indicator.opacity == 1
    
    # Testa fim do loading
    pesquisa_screen.show_loading(False)
    assert pesquisa_screen.loading_indicator.opacity == 0