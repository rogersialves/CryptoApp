from setuptools import setup, find_packages

setup(
    name="cryptoapp",
    version="0.1",
    description="Aplicativo para controle de carteira de criptomoedas",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'kivy>=2.2.1',
        'pytest>=7.4.3',
        'pytest-cov>=4.1.0',  # Para cobertura de testes
        'python-dotenv>=1.0.0',
        'requests>=2.31.0',   # Para futuras chamadas de API
        'pandas>=2.1.0',      # Para análise de dados
    ],
    extras_require={
        'dev': [
            'black',          # Formatador de código
            'flake8',        # Linter
            'isort',         # Organizador de imports
            'mypy',          # Verificador de tipos
        ],
        'test': [
            'pytest-mock',    # Para mock em testes
            'pytest-asyncio', # Para testes assíncronos
        ],
    },
    entry_points={
        'console_scripts': [
            'cryptoapp=src.main:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
)