# CryptoApp

![CI](https://github.com/seu-usuario/cryptoapp/workflows/CI/badge.svg)
![Coverage](https://codecov.io/gh/seu-usuario/cryptoapp/branch/main/graph/badge.svg)

Aplicativo para controle de carteira de criptomoedas desenvolvido em Python usando Kivy.

## 📋 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/cryptoapp.git
cd cryptoapp
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Instale o pacote e suas dependências:
```bash
# Instalação básica
pip install -e .

# Instalação com ferramentas de desenvolvimento
pip install -e ".[dev]"

# Instalação com ferramentas de teste
pip install -e ".[test]"
```

## 💻 Uso

Para iniciar o aplicativo:

```bash
python main.py
```

Ou usando o entry point instalado:

```bash
cryptoapp
```

### Funcionalidades

- Adicionar transações de criptomoedas
- Visualizar portfólio atual
- Acompanhar histórico de transações
- Calcular preço médio por moeda

## 🧪 Testes

Para executar os testes:

```bash
# Executar todos os testes
python -m pytest

# Executar testes com cobertura
python -m pytest --cov=src

# Gerar relatório de cobertura HTML
python -m pytest --cov=src --cov-report=html
```

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
CryptoApp/
├── src/
│   ├── __init__.py
│   ├── portfolio.py
│   ├── data_manager.py
│   └── ui.py
├── tests/
│   ├── __init__.py
│   ├── test_portfolio.py
│   └── test_ui.py
├── main.py
├── setup.py
├── LICENSE
└── README.md
```

### Ferramentas de Desenvolvimento

- **black**: Formatação de código
- **flake8**: Linting
- **isort**: Organização de imports
- **mypy**: Verificação de tipos

Para formatar o código:
```bash
black src tests
isort src tests
flake8 src tests
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## ✨ Próximos Passos

- [ ] Integração com APIs de preços de criptomoedas
- [ ] Gráficos de desempenho do portfólio
- [ ] Exportação de relatórios
- [ ] Suporte a múltiplas moedas
