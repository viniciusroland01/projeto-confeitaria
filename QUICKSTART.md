# ⚡ Quick Start - Fernanda Doces

## 📥 Instalação (30 segundos)

### Windows
```bash
setup.bat
python manage.py createsuperuser
python manage.py runserver
```

### Linux/Mac
```bash
bash setup.sh
python manage.py createsuperuser
python manage.py runserver
```

Visite: http://localhost:8000

---

## 🔑 Credenciais

| URL | Acesso |
|-----|--------|
| `/` | Vitrine pública |
| `/admin/` | Painel de controle |

---

## 📝 Adicionar Produtos

1. Vá para http://localhost:8000/admin
2. Login com sua conta criada
3. Clique em "Doces"
4. Clique em "Add Doce"
5. Preencha: Nome, Preço, Imagem
6. Clique "Save"
7. Pronto! Aparece na vitrine

---

## 💼 Gerenciar Clientes

1. No admin, clique em "Perfis"
2. Procure o cliente
3. Use ações:
   - **Confirmar Pedido**: +2 pontos
   - **Usar Recompensa**: -20 pontos

---

## 🌐 Fazer Deploy

### Opção 1: Railway (Fácil)
```bash
git push origin main
# Railway faz deploy automático
```

### Opção 2: Seu PC
```bash
# Já está pronto!
python manage.py runserver 0.0.0.0:8000
# Acesse de qualquer IP da rede
```

Veja **DEPLOY.md** para detalhes.

---

## 📂 Estrutura Rápida

```
📁 fernanda_doces/
  📁 catalogo/        ← Produtos & Carrinho
  📁 usuarios/        ← Login & Perfil
  📁 templates/       ← HTML (base.html aqui)
  📁 static/css/      ← CSS
  📁 media/           ← Imagens de produtos
  core/settings.py    ← Configurações
  manage.py           ← Django CLI
```

---

## 🎨 Customizar Cores

Em `static/css/style.css`, altere:

```css
:root {
    --rosa-dark: #ad1457;      /* Cor escura */
    --rosa-principal: #ec407a;  /* Cor principal */
    --rosa-claro: #fce4ec;      /* Cor clara */
}
```

---

## 🤖 Alterar WhatsApp

Em `catalogo/views.py`, procure por:

```python
link_whatsapp = f"https://wa.me/5532984069242?text={texto_final}"
                                      ^^^^^^
                        Coloque seu número aqui
```

---

## 🐛 Problemas Comuns

| Problema | Solução |
|----------|---------|
| "Module not found" | `pip install -r requirements.txt` |
| Imagens não aparecem | `python manage.py collectstatic` |
| Login não funciona | Crie novo superuser: `createsuperuser` |
| CSS não atualiza | Atualize o navegador (Ctrl+Shift+R) |

---

## 📊 Monitoramento

Ver logs em tempo real:
```bash
python manage.py runserver
```

Ver banco de dados:
```bash
python manage.py dbshell
```

---

## 🔐 Variáveis de Ambiente

Crie arquivo `.env`:
```env
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=sua-chave-secreta
ALLOWED_HOSTS=localhost,127.0.0.1
```

---

## ⚙️ Comandos Essenciais

```bash
# Setup
python manage.py migrate           # Aplica migrações
python manage.py createsuperuser   # Novo admin

# Admin
python manage.py runserver         # Inicia servidor
python manage.py shell             # Python interativo com Django

# Manutenção
python manage.py makemigrations    # Cria migração
python manage.py collectstatic     # Coleta CSS/JS
python manage.py dumpdata > bak.json  # Backup
python manage.py loaddata bak.json    # Restore
```

---

## 📚 Documentação Completa

- **README.md** - Setup e features
- **DEPLOY.md** - Como fazer deploy
- **CONTRIBUTING.md** - Padrões de código
- **CHANGELOG.md** - Histórico de versões
- **SUMMARY.md** - Resumo das alterações
- **.env.example** - Variáveis de ambiente

---

## 💡 Dicas

✅ **Backup regularmente:**
```bash
python manage.py dumpdata > backup.json
```

✅ **Atualizar dependências:**
```bash
pip install --upgrade -r requirements.txt
```

✅ **Testar segurança:**
```bash
python manage.py check --deploy
```

---

## 🚀 Status

✅ Pronto para desenvolvimento  
✅ Pronto para produção  
✅ Documentação completa  
✅ Sem bugs conhecidos  

---

**Precisa de ajuda?** Veja os arquivos `.md` ou entre em contato!

🍰 **Boa sorte com o Fernanda Doces!**
