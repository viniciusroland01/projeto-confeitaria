# 🍰 Sistema de Confeitaria - Fernanda Doces

Este é um ecossistema completo para gestão de vendas de uma confeitaria, evoluindo de uma landing page estática para uma aplicação Web robusta utilizando o framework **Django**.

## 🚀 Diferenciais Técnicos (Backend)

Funcionalidades :

- **Sistema de Fidelidade:** O modelo de `Perfil` rastreia pontos acumulados por cada usuário (Lógica: 20 pts = 1 brinde), incentivando a retenção de clientes.
- **Gestão de Catálogo:** Administração total via Django Admin, permitindo cadastrar, atualizar preços e controlar disponibilidade de produtos em tempo real.
- **Segurança de Dados:** Uso de `python-decouple` para ocultar chaves sensíveis (Secret Keys) e `whitenoise` para servir arquivos estáticos de forma eficiente.
- **Manipulação de Imagens:** Integração com a biblioteca `Pillow` para processamento de fotos dos produtos.
- **Relacionamento de Dados:** Uso de `OneToOneField` para estender o modelo de usuário padrão do Django.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** Django 4.2.7 (MVT Architecture)
- **Banco de Dados:** SQLite (Desenvolvimento)
- **Servidor de Produção:** Gunicorn & Whitenoise
- **Frontend:** HTML5, CSS3, JavaScript (Integração WhatsApp API)

## 📋 Funcionalidades Principais

- [x] **Catálogo Dinâmico:** Listagem de doces com preços e fotos vindos do banco de dados.
- [x] **Área do Cliente:** Cadastro e login de usuários com perfil personalizado.
- [x] **Painel Administrativo:** Interface para o dono do negócio gerenciar o estoque.
- [x] **Status de Disponibilidade:** Produtos podem ser marcados como "Indisponíveis" sem precisar deletá-los.

## 🔧 Como Rodar o Projeto

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/viniciusroland01/projeto-confeitaria.git](https://github.com/viniciusroland01/projeto-confeitaria.git)
