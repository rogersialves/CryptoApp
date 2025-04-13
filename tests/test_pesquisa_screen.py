import pytest
from unittest.mock import Mock, patch
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from src.screens.pesquisa_screen import PesquisaScreen, LoadingIndicator
from src.core.theme import FONTS
from src.api.crypto import search_crypto

@pytest.fixture
def pesquisa_screen(kivy_app):
    """Fixture que fornece uma tela de pesquisa inicializada"""
    screen = PesquisaScreen()
    return screen

def test_init_pesquisa_screen(pesquisa_screen):
    """Testa se a tela é inicializada corretamente"""
    assert isinstance(pesquisa_screen, MDScreen)
    
    # Verifica título
    title_style = FONTS["title"]
    assert pesquisa_screen.title.text == "Pesquisar"
    assert pesquisa_screen.title.font_size == title_style["font_size"]
    assert pesquisa_screen.title.font_style == title_style["font_style"]
    assert pesquisa_screen.title.theme_text_color == title_style["theme_text_color"]
    
    # Verifica campo de pesquisa
    assert hasattr(pesquisa_screen, 'search_field')
    
    # Verifica estado inicial
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
    """Testa fluxo completo de pesquisa"""
    mock_results = [{"symbol": "BTC", "name": "Bitcoin"}]
    
    async def mock_search(*args):
        return mock_results
    
    with patch('src.screens.pesquisa_screen.search_crypto', new=mock_search):
        # Simula pesquisa
        pesquisa_screen.on_search(None, "bitcoin")
        await pesquisa_screen._do_search()
        
        # Verifica resultados
        assert "bitcoin" in pesquisa_screen._cache
        assert len(pesquisa_screen.results_list.children) > 0

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
    
    # Exibe erro
    pesquisa_screen.show_error(error_msg)
    
    # Verifica mensagem
    assert len(pesquisa_screen.results_list.children) == 1
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
    """Testa tratamento de erro na pesquisa"""
    error_msg = "Erro de API"
    
    # Mock para simular erro
    async def mock_search_error(*args):
        raise Exception(error_msg)
    
    with patch('src.api.crypto.search_crypto', side_effect=mock_search_error):
        pesquisa_screen._last_search = "error"
        await pesquisa_screen._do_search()
        
        # Verifica mensagem de erro
        label = pesquisa_screen.results_list.children[0]
        assert isinstance(label, MDLabel)
        assert error_msg in label.text
        assert "Erro na pesquisa:" in label.text
        assert label.theme_text_color == "Error"
        assert label.font_size == FONTS["body"]["font_size"]

def test_loading_indicators(pesquisa_screen):
    """Testa indicadores de carregamento"""
    # Testa início do loading
    pesquisa_screen.show_loading(True)
    assert pesquisa_screen.loading_indicator.opacity == 1
    
    # Testa fim do loading
    pesquisa_screen.show_loading(False)
    assert pesquisa_screen.loading_indicator.opacity == 0