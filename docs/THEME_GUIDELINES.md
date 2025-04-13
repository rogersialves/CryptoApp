# Guia de Boas Práticas: Temas e Estilos

## 📚 Sumário
1. [Estrutura de Temas](#estrutura-de-temas)
2. [Configuração de Fontes](#configuração-de-fontes)
3. [Testes](#testes)
4. [Boas Práticas](#boas-práticas)

## Estrutura de Temas

### Padrões de Configuração
```python
FONTS = {
    "display": {
        "font_name": "Roboto",
        "font_style": "Body1",
        "theme_text_color": "Primary",
        "font_size": 34,
        "font_style_name": "Display"
    }
}
```

### Propriedades Obrigatórias
- `font_name`: Nome da fonte base
- `font_style`: Estilo KivyMD válido
- `theme_text_color`: Cor do tema
- `font_size`: Valor numérico (não usar strings)
- `font_style_name`: Identificador interno

## Configuração de Fontes

### Tamanhos Padrão
- Display: 34
- Title: 20
- Subtitle: 14
- Body: 16
- Caption: 12

### Cores do Tema
- Primary
- Secondary
- Error
- ContrastParentBackground

## Testes

### Fixtures Essenciais
```python
@pytest.fixture(scope="session")
def kivy_app():
    """Fixture do app para testes"""

@pytest.fixture
def font_styles():
    """Fixture de estilos de fonte"""
```

### Validações Necessárias
1. Existência de propriedades
2. Tipos de dados corretos
3. Valores dentro dos limites
4. Fallback apropriado

## Boas Práticas

### Geral
1. Use valores numéricos para `font_size`
2. Mantenha um estilo de fallback
3. Valide todas as propriedades
4. Documente alterações

### Testes
1. Isole testes de UI
2. Use fixtures reutilizáveis
3. Implemente validações completas
4. Trate exceções adequadamente

### Performance
1. Cache de estilos quando possível
2. Reutilize instâncias do app
3. Minimize criação de widgets

## 🔍 Troubleshooting

### Problemas Comuns
1. Erro de KeyError em estilos
   - Solução: Verificar nome do estilo
   - Usar fallback apropriado

2. Tipo incorreto de font_size
   - Solução: Usar valores numéricos
   - Evitar strings com 'sp'

### Dicas de Depuração
1. Use logging apropriado
2. Verifique stack traces
3. Valide configs antes do uso