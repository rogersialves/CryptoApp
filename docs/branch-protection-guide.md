# Guia: Configurando Proteções de Branch no GitHub

## Pré-requisitos
- Acesso de administrador ao repositório
- Repositório já criado no GitHub
- Branch `main` já existente

## Passos para Configuração

### 1. Acessar Configurações
1. Abra [CryptoApp Settings](https://github.com/rogersialves/CryptoApp/settings)
2. Navegue até "Settings" no menu superior
3. [Adicionar screenshot aqui]

### 2. Configurar Branch Protection
1. Clique em "Branches" no menu lateral
2. Clique em "Add branch protection rule"
3. [Adicionar screenshot aqui]

### 3. Regras de Proteção
Configure as seguintes opções:
```yaml
Branch name pattern: main
Options:
  ✓ Require a pull request before merging
    ✓ Require approvals (1)
  ✓ Require status checks to pass before merging
  ✓ Include administrators
```
[Adicionar screenshot aqui]

### 4. Salvar Configurações
1. Role até o final da página
2. Clique em "Create"
3. [Adicionar screenshot aqui]

## Verificação

Para testar as proteções:
```powershell
# Tente fazer push direto para main (deve falhar)
git checkout main
git push origin main

# Crie uma branch de teste
git checkout -b test/protection
git commit --allow-empty -m "test: verifica proteção"
git push origin test/protection
```

## Observações
- Mantenha screenshots atualizados
- Documente alterações nas regras
- Revise periodicamente as configurações