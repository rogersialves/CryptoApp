# CryptoApp

Aplicativo de criptomoedas desenvolvido com Python, Kivy e KivyMD.

## Status do Projeto

🚧 Em desenvolvimento 

## Funcionalidades Implementadas

- [x] Lista de criptomoedas com preços atualizados
- [x] Layout base com navegação lateral
- [x] Tela de portfólio básica
- [x] Conversor de moedas (estrutura básica)
- [x] Integração inicial com CoinGecko API

## Próximos Passos

1. Corrigir bugs de UI/UX
   - Resolver problemas com TopAppBar
   - Ajustar espaçamentos e layouts
   - Corrigir estilos dos botões
   - Implementar temas claro/escuro
   - Adicionar feedback visual para ações

2. Implementar lógica do conversor
   - Integrar API de cotações em tempo real
   - Adicionar histórico de conversões
   - Implementar cache de resultados
   - Adicionar gráficos de variação

3. Melhorar tratamento de erros
   - Implementar sistema de logs estruturado
   - Adicionar recuperação de falhas
   - Melhorar mensagens de erro
   - Criar sistema de retry para chamadas API

4. Estrutura e Organização
   - Implementar padrão de injeção de dependências
   - Criar gerenciamento de estado centralizado
   - Separar lógica de negócio da UI
   - Organizar constantes e configurações

5. Infraestrutura
   - Configurar CI/CD (GitHub Actions)
   - Implementar versionamento semântico
   - Criar processo de build automatizado
   - Preparar para distribuição

6. Documentação
   - Documentar arquitetura do projeto
   - Criar guia de contribuição
   - Adicionar docstrings em classes/métodos
   - Documentar APIs e integrações

7. Testes
   - Implementar testes unitários
   - Adicionar testes de integração
   - Configurar cobertura de código
   - Criar testes de UI automatizados

8. Otimização
   - Implementar cache de dados
   - Melhorar performance geral
   - Reduzir uso de memória
   - Otimizar chamadas de rede

9. Novas Funcionalidades
   - Implementar sistema de alertas
   - Adicionar notificações push
   - Criar dashboard personalizado
   - Integrar mais fontes de dados
   - Implementar sistema de carteiras e corretoras:
     * Integração com APIs de corretoras principais (Binance, Coinbase, etc)
     * Suporte para carteiras via endereço público (BTC, ETH, etc)
     * Monitoramento de saldo em tempo real
     * Histórico de transações
     * Alertas de movimentação
     * Suporte para múltiplas carteiras
     * Exportação de relatórios
     * Integração com DeFi protocols
     * Rastreamento de NFTs
     * Análise de gas fees

10. Segurança e Privacidade
    - Implementar criptografia de dados sensíveis
    - Adicionar autenticação 2FA
    - Criar sistema de backup de dados
    - Implementar validação de endereços
    - Proteção contra phishing
    - Auditoria de segurança

## Estrutura do Projeto

```
CryptoApp/
├── .venv/                      # Ambiente virtual Python
├── .vscode/                    # Configurações do VS Code
│   └── settings.json
├── src/
│   ├── screens/               # Telas do aplicativo
│   │   ├── __init__.py
│   │   ├── base_screen.py     # Classe base para todas as telas
│   │   ├── lista_screen.py    # Tela de listagem de criptomoedas
│   │   ├── portfolio_screen.py # Tela de portfólio
│   │   ├── conversor_screen.py # Tela do conversor
│   │   ├── alertas_screen.py   # Tela de alertas
│   │   ├── pesquisa_screen.py  # Tela de pesquisa
│   │   └── noticias_screen.py  # Tela de notícias
│   ├── services/              # Serviços e APIs
│   │   ├── __init__.py
│   │   ├── coingecko_service.py # Integração com CoinGecko
│   │   └── cache_service.py     # Serviço de cache (planejado)
│   ├── models/                # Modelos de dados
│   │   ├── __init__.py
│   │   └── portfolio.py       # Modelo do portfólio
│   └── utils/                 # Utilitários
│       ├── __init__.py
│       └── constants.py       # Constantes do projeto
├── tests/                     # Testes unitários
│   ├── __init__.py
│   ├── test_portfolio.py
│   └── test_coingecko.py
├── docs/                      # Documentação
│   ├── architecture.md
│   └── api.md
├── .gitignore                # Arquivos ignorados pelo Git
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências do projeto
├── requirements-dev.txt      # Dependências de desenvolvimento
└── main.py                  # Ponto de entrada do aplicativo
```

### Descrição dos Diretórios

- `.venv/`: Ambiente virtual Python para isolamento de dependências
- `.vscode/`: Configurações específicas do VS Code
- `src/`: Código-fonte principal do aplicativo
  - `screens/`: Telas e interfaces do usuário
  - `services/`: Integrações com serviços externos
  - `models/`: Modelos e estruturas de dados
  - `utils/`: Funções utilitárias e constantes
- `tests/`: Testes automatizados
- `docs/`: Documentação do projeto

### Arquivos Principais

- `main.py`: Arquivo principal que inicia o aplicativo
- `requirements.txt`: Lista de dependências para produção
- `requirements-dev.txt`: Dependências adicionais para desenvolvimento
- `.gitignore`: Configuração de arquivos ignorados pelo Git

## Tecnologias Utilizadas

- Python 3.x
- Kivy
- KivyMD 2.0
- CoinGecko API

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/CryptoApp.git
```

2. Instale as dependências:
```bash
pip install kivy kivymd requests
```

3. Execute o aplicativo:
```bash
python main.py
```

## Requisitos Mínimos

- Windows 10/11 ou Linux/MacOS
- Python 3.9+
- 4GB RAM
- 500MB espaço em disco
- Conexão com internet

## Ambiente de Desenvolvimento

1. Criar ambiente virtual:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/MacOS
```

2. Instalar dependências de desenvolvimento:
```bash
pip install -r requirements-dev.txt
```

3. Configurar VS Code:
   - Instalar extensão Python
   - Instalar extensão Pylint
   - Configurar formatador (Black)

## Estrutura de Branches

- `main`: Versão estável
- `develop`: Branch de desenvolvimento
- `feature/*`: Novas funcionalidades
- `bugfix/*`: Correções de bugs
- `release/*`: Preparação para release

## Convenções de Código

- PEP 8 para estilo Python
- Docstrings em todas as classes/métodos
- Type hints para tipos de dados
- Testes para novas funcionalidades
- Commits semânticos

## Recursos Úteis

- [Documentação do Kivy](https://kivy.org/doc/stable/)
- [KivyMD Components](https://kivymd.readthedocs.io/en/latest/components/)
- [CoinGecko API](https://www.coingecko.com/api/documentation)
- [Python Clean Code](https://github.com/zedr/clean-code-python)

## FAQ

1. **Como atualizar as dependências?**
```bash
pip install --upgrade -r requirements.txt
```

2. **Como executar os testes?**
```bash
python -m pytest tests/
```

3. **Como gerar documentação?**
```bash
cd docs
mkdocs serve
```

4. **Como reportar bugs?**
Abra uma issue usando o template disponível

## Logs e Notificações

O sistema usa diferentes níveis de log para notificações:

### Níveis de Log

```python
[INFO   ] # Informações gerais do sistema
[DEBUG  ] # Informações detalhadas para desenvolvimento
[ERROR  ] # Erros e exceções do sistema
```

### Exemplos de Uso

```python
# Informações
[INFO   ] [Base        ] Start application main loop
[INFO   ] [Window      ] Provider: sdl2

# Debugging
[DEBUG  ] [Cache       ] register <textinput.width>
[DEBUG  ] [Resource    ] add path: C:\Users\...\fonts

# Erros
[ERROR  ] [Erro na inicialização] 'PortfolioScreen' object has no attribute 'portfolio'
[ERROR  ] [Erro ao carregar dados] 'ListaScreen' object has no attribute 'coingecko'
```

### Configuração de Logs

O nível de log pode ser configurado no arquivo `main.py`:

```python
from kivy.logger import Logger
Logger.setLevel('DEBUG')  # Níveis: DEBUG, INFO, WARNING, ERROR
```

## Contribuição

Por favor, leia o guia de contribuição antes de submeter pull requests.

## Contato

- Email: seu-email@exemplo.com
- Discord: link-do-servidor
- Twitter: @seu-usuario

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
