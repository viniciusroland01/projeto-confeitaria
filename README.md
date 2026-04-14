# 🍰 Fernanda Doces - E-commerce & Loja Digital

Sistema de e-commerce profissional desenvolvido em **Django** para a **Fernanda Doces**, com integração WhatsApp, sistema de pontos de fidelidade e admin customizado.

## ✨ Features

✅ **Catálogo Digital** - Exibição profissional de produtos com imagens  
✅ **Carrinho de Compras** - Com controle de quantidade e recálculo automático  
✅ **Sistema de Pontos** - Fidelidade do cliente (20 pts = 1 brinde)  
✅ **Integração WhatsApp** - Envio automático de pedidos  
✅ **Autenticação de Usuários** - Login e cadastro seguro  
✅ **Admin Customizado** - Painel para gerenciar produtos e recompensas  
✅ **Design Responsivo** - Otimizado para desktop e mobile  
✅ **Segurança** - CSRF, validação de senha, proteção contra XSS  

## 🛠️ Tecnologias

- **Backend:** Django 4.2.7
- **Frontend:** HTML5 + CSS3 + JavaScript (Vanilla)
- **Banco de Dados:** SQLite (desenvolvimento) / PostgreSQL (produção)
- **Deploy:** Railway/Heroku compatible
- **Imagens:** Pillow
- **Servidor:** Gunicorn + WhiteNoise

## 📋 Pré-requisitos

- Python 3.8+
- pip ou poetry
- Git (opcional)

## 🚀 Instalação & Setup

### 1. Clone o repositório
```bash
git clone <seu-repositorio>
cd fernanda_doces
```

### 2. Crie e ative um ambiente virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
```bash
# Copie o arquivo exemplo
cp .env.example .env

# Edite o .env com suas configurações
# (SECRET_KEY, DEBUG, etc)
```

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário
```bash
python manage.py createsuperuser
# Digite: username, email, password
```

### 7. Carregue dados de exemplo (opcional)
```bash
python manage.py loaddata initial_data
```

### 8. Inicie o servidor
```bash
python manage.py runserver
```

Acesse: **http://localhost:8000**

## 📂 Estrutura do Projeto

```
fernanda_doces/
├── core/                  # Configurações principais
│   ├── settings.py       # Configuração do Django
│   ├── urls.py           # URLs principais
│   └── wsgi.py           # Configuração de produção
├── catalogo/             # App de produtos
│   ├── models.py         # Model Doce
│   ├── views.py          # Lógica de catálogo e carrinho
│   ├── urls.py           # Rotas
│   └── templates/        # Templates do catálogo
├── usuarios/             # App de autenticação
│   ├── models.py         # Model Perfil (fidelidade)
│   ├── views.py          # Login, Cadastro
│   ├── urls.py           # Rotas de autenticação
│   └── templates/        # Templates de auth
├── templates/            # Templates reutilizáveis
│   └── base.html         # Template base
├── static/               # CSS, JS, imagens
│   └── css/style.css     # Estilos principais
├── media/                # Uploads (imagens de produtos)
├── manage.py             # Gerenciador Django
├── requirements.txt      # Dependências Python
├── .env.example          # Variáveis de ambiente (exemplo)
└── README.md             # Este arquivo
```

## 🔐 Configuração de Segurança

### Variáveis de Ambiente Importantes

```env
# Desenvolvimento
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=sua-chave-secreta

# Produção
DJANGO_DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

### Em Produção (Railway/Heroku)
- DEBUG = False
- ALLOWED_HOSTS configurado
- CSRF_TRUSTED_ORIGINS definido
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True

## 💳 Integração WhatsApp

O sistema envia automaticamente mensagens formatadas para o WhatsApp. Atualize o número:

**Em `catalogo/views.py` - função `finalizar_pedido()`:**
```python
link_whatsapp = f"https://wa.me/5532984069242?text={texto_final}"
```

## 👤 Admin Customizado

Acesse: **http://localhost:8000/admin**

### Gerenciar Produtos
- Adicionar/editar doces
- Mostrar/ocultar (campo "disponível")
- Upload de imagens

### Gerenciar Clientes & Pontos
- Buscar clientes
- Confirmar pedidos (+2 pontos)
- Resgatar recompensas (-20 pontos)

## 🌐 Deploy no Railway

### 1. Prepare o projeto
```bash
pip freeze > requirements.txt
git add .
git commit -m "Ready for production"
```

### 2. Configure no Railway
- Conecte seu repositório GitHub
- Configure variáveis de ambiente no painel
- Deploy automático!

### 3. Rode migrações em produção
```bash
railway run python manage.py migrate
railway run python manage.py collectstatic --noinput
```

## 🐛 Troubleshooting

### Erro: "Module not found"
```bash
pip install -r requirements.txt
```

### Erro: "Static files not found"
```bash
python manage.py collectstatic --noinput
```

### Erro: "Database locked"
```bash
rm db.sqlite3
python manage.py migrate
```

### Reset completo do banco
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📞 Suporte & Contato

Desenvolvido por **Vinícius Roland**

WhatsApp: [Contate aqui](https://wa.me/5532988366586)

## 📄 Licença

Este projeto é propriedade intelectual de Fernanda Doces.

---

**Versão:** 1.0.0  
**Última atualização:** 2026
