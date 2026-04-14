# Padrões de Desenvolvimento - Fernanda Doces

## 📝 Guia de Contribuição

Se você está desenvolvendo este projeto, siga estes padrões para manter o código profissional e mantenível.

## 🎯 Convenções de Código

### Python/Django

#### Models
```python
class MinhaModel(models.Model):
    # Sempre use verbose_name e help_text
    campo = models.CharField(
        max_length=100,
        verbose_name='Nome do Campo',
        help_text='Descrição breve'
    )
    
    # Sempre defina Meta com verbose_name_plural
    class Meta:
        verbose_name = 'Minha Model'
        verbose_name_plural = 'Minhas Models'
        ordering = ['-criado_em']
    
    # __str__ sempre deve retornar algo legível
    def __str__(self):
        return f"{self.nome} - {self.id}"
```

#### Views
```python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

def minha_view(request):
    # Valide os dados de entrada
    if request.method == 'POST':
        dados = request.POST.get('campo', '')
        if not dados:
            messages.error(request, 'Campo obrigatório!')
            return render(request, 'template.html')
    
    # Use try/except para operações do banco
    try:
        objeto = MinhaModel.objects.get(id=1)
    except MinhaModel.DoesNotExist:
        messages.error(request, 'Objeto não encontrado')
        return redirect('home')
    
    return render(request, 'template.html', {'objeto': objeto})
```

### HTML/Templates

```html
{% extends "base.html" %}
{% load static %}

{% block title %}Título da página{% endblock %}

{% block content %}
<div class="container">
    <!-- Use semantic HTML -->
    <h1>Título</h1>
    <p>Conteúdo</p>
</div>
{% endblock %}
```

### CSS

```css
/* Use variáveis CSS quando possível */
:root {
    --cor-principal: #ec407a;
    --cor-destaque: #ad1457;
}

/* Mobile first approach */
.elemento {
    width: 100%;
    padding: 10px;
}

@media (min-width: 768px) {
    .elemento {
        width: 50%;
        padding: 20px;
    }
}
```

## 🗂️ Estrutura de Arquivos

### URLs
```python
# Core URLs - apenas inclusão de apps
urlpatterns = [
    path('', include('catalogo.urls')),
    path('usuarios/', include('usuarios.urls')),
]

# App URLs - rotas específicas
urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:id>/', views.detalhe, name='detalhe'),
]
```

### Templates
```
templates/
├── base.html              # Template base (navbar, footer)
├── catalogo/
│   ├── home.html
│   └── carrinho.html
└── usuarios/
    ├── login.html
    └── cadastro.html
```

## 🔍 Segurança

- ✅ Sempre use `{% csrf_token %}` em formulários
- ✅ Nunca coloque dados sensíveis em JavaScript
- ✅ Use `strip_tags()` para limpar input do usuário
- ✅ Configure ALLOWED_HOSTS em produção
- ✅ Nunca commit `.env` com dados sensíveis
- ✅ Use `get_object_or_404()` em vez de `.get()`

## 📊 Boas Práticas

### Banco de Dados
```python
# ❌ Ruim - N+1 query
for doce in Doce.objects.all():
    print(doce.categoria.nome)  # Faz query pra cada doce

# ✅ Bom - select_related
doces = Doce.objects.select_related('categoria')
```

### Queryset
```python
# ✅ Sempre filtre antes de paginar
doces = Doce.objects.filter(disponivel=True).order_by('-preco')

# ✅ Use values() para dados simples
nomes = Doce.objects.values_list('nome', flat=True)
```

### Templates
```html
<!-- ❌ Ruim - lógica complexa no template -->
{% if objeto.preco > 50 and objeto.categoria == 'premium' %}

<!-- ✅ Bom - lógica na view -->
{% if objeto.eh_premium %}
```

## 🧪 Testing

```python
from django.test import TestCase
from .models import Doce

class DoceTestCase(TestCase):
    def setUp(self):
        Doce.objects.create(
            nome='Bolo de Chocolate',
            preco=25.00
        )
    
    def test_str_representation(self):
        doce = Doce.objects.get(nome='Bolo de Chocolate')
        self.assertEqual(str(doce), 'Bolo de Chocolate - 25.00')
```

## 📋 Checklist para Commits

Antes de fazer commit, verifique:

- [ ] Código sem erros de sintaxe
- [ ] Variáveis significativas (não `a`, `b`, `x`)
- [ ] Comentários em português em código complexo
- [ ] Sem hard-coded sensitive data (senhas, chaves)
- [ ] Sem arquivos de debug ou temporários
- [ ] Docstrings em funções público
- [ ] Testes passando (se houver)

## 🔧 Comum

### Adicionar novo campo a Model
1. Adicione o campo em `models.py`
2. Crie migração: `python manage.py makemigrations`
3. Aplique: `python manage.py migrate`
4. Atualize admin se necessário

### Criar nova View
1. Defina em `views.py`
2. Adicione rota em `urls.py`
3. Crie template em `templates/app/`
4. Adicione ao menu/navbar se necessário

## 📞 Dúvidas?

Veja [Django Docs](https://docs.djangoproject.com/) ou entre em contato com o time.
