import pytest
import sys
from pathlib import Path
from kivymd.app import MDApp

# Adiciona o diretório raiz ao PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

class MockApp(MDApp):
    def __init__(self):
        super().__init__()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"

@pytest.fixture
def mock_app(monkeypatch):
    """Fornece um mock do MDApp"""
    app = MockApp()
    app._running = True
    monkeypatch.setattr('kivymd.app.MDApp.get_running_app', lambda: app)
    return app