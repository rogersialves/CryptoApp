from setuptools import setup, find_packages

setup(
    name="cryptoapp",
    version="0.1.0",
    description="Aplicativo para controle de carteira de criptomoedas",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        "kivy>=2.0.0",
        "kivymd>=1.1.1",
        "requests>=2.26.0",
        "python-binance>=1.0.15"
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "isort",
            "mypy",
        ],
        "test": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "cryptoapp=src.main:main",
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