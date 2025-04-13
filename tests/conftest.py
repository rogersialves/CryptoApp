import pytest
import asyncio
import sys   
from kivy.logger import Logger
from functools import wraps
from pathlib import Path
from kivymd.app import MDApp

# Adiciona o diretório raiz ao PYTHONPATH
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

def async_test(f):
    """Decorator para testes assíncronos"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(f(*args, **kwargs))
    return wrapper

@pytest.fixture(scope="session")
def event_loop():
    """Fixture para gerenciar event loop"""
    policy = asyncio.WindowsProactorEventLoopPolicy()
    asyncio.set_event_loop_policy(policy)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    
    # Limpa tasks pendentes
    pending = asyncio.all_tasks(loop)
    for task in pending:
        task.cancel()
    
    # Fecha o loop adequadamente    
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()

@pytest.fixture
def kivy_app():
    """Fixture para inicializar o app KivyMD nos testes"""
    app = MDApp()
    app.theme_cls.theme_style = "Light"
    return app

@pytest.fixture(autouse=True)
def init_app(kivy_app):
    """Fixture que garante que o app está inicializado para todos os testes"""
    kivy_app.theme_cls.primary_palette = "Blue"
    yield kivy_app

@pytest.fixture(autouse=True)
def setup_teardown(event_loop):
    """Fixture para setup/teardown de cada teste"""
    # Setup
    Logger.setLevel('ERROR')  # Reduz logs
    
    yield
    
    # Teardown
    if event_loop.is_running():
        event_loop.stop()