from django.shortcuts import render, get_object_or_404, redirect
from .models import Doce
import urllib.parse

# 1. HOME (Exibição da vitrine de doces)
def home(request):
    doces = Doce.objects.all()
    return render(request, 'catalogo/home.html', {'doces': doces})

# 2. ADICIONAR AO CARRINHO (Com suporte a POST da Home)
def adicionar_ao_carrinho(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    
    quantidade = 1
    if request.method == 'POST':
        try:
            quantidade = int(request.POST.get('quantidade', 1))
            if quantidade < 1:
                quantidade = 1
        except ValueError:
            quantidade = 1
        
    carrinho[id_str] = carrinho.get(id_str, 0) + quantidade
    request.session['carrinho'] = carrinho
    request.session.modified = True
    
    referencia = request.META.get('HTTP_REFERER', '')
    if 'carrinho' in referencia:
        return redirect('ver_carrinho')
    return redirect('home')

# 3. VER CARRINHO (Calcula o total e limpa itens deletados do banco)
def ver_carrinho(request):
    carrinho_sessao = request.session.get('carrinho', {})
    itens_carrinho = []
    total_geral = 0
    ids_para_remover = []

    for doce_id, quantidade in carrinho_sessao.items():
        try:
            doce = Doce.objects.get(id=doce_id)
            qtd = int(quantidade)
            subtotal = doce.preco * qtd
            total_geral += subtotal
            itens_carrinho.append({'doce': doce, 'quantidade': qtd, 'subtotal': subtotal})
        except (Doce.DoesNotExist, ValueError):
            ids_para_remover.append(doce_id)

    if ids_para_remover:
        for id_remover in ids_para_remover:
            if id_remover in carrinho_sessao:
                del carrinho_sessao[id_remover]
        request.session.modified = True

    return render(request, 'catalogo/carrinho.html', {'itens': itens_carrinho, 'total': total_geral})

# 4. REMOVER DO CARRINHO (Diminui quantidade)
def remover_do_carrinho(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    
    if id_str in carrinho:
        carrinho[id_str] -= 1
        if carrinho[id_str] <= 0:
            del carrinho[id_str]
        request.session['carrinho'] = carrinho
        request.session.modified = True
    
    return redirect('ver_carrinho')

# 5. EXCLUIR ITEM (Remove o item completamente do carrinho)
def excluir_item(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    
    if id_str in carrinho:
        del carrinho[id_str]
        request.session['carrinho'] = carrinho
        request.session.modified = True
    
    return redirect('ver_carrinho')

# 6. FINALIZAR PEDIDO (Gera WhatsApp e deixa pontos para a Fernanda validar)
def finalizar_pedido(request):
    carrinho_sessao = request.session.get('carrinho', {})
    
    if not carrinho_sessao:
        return redirect('home')
    
    texto = "📦 NOVO PEDIDO - FERNANDA DOCES 📦\n\n"
    total = 0
    itens_formatados = ""

    for doce_id, qtd in carrinho_sessao.items():
        try:
            doce = Doce.objects.get(id=doce_id)
            quantidade = int(qtd)
            subtotal = doce.preco * quantidade
            total += subtotal
            itens_formatados += f"🧁 {quantidade}x {doce.nome} - R$ {subtotal:.2f}\n"
        except (Doce.DoesNotExist, ValueError):
            continue 

    texto += itens_formatados
    texto += f"\n💵 TOTAL DO PEDIDO: R$ {total:.2f}"
    texto += f"\n--------------------------\n"

    # Identificação do Cliente (Sem alteração de pontos automática)
    if request.user.is_authenticated:
        texto += f"👤 Cliente: {request.user.username}\n"
        if hasattr(request.user, 'perfil'):
            texto += f"⭐ Saldo Atual: {request.user.perfil.pontos} pts\n"
    else:
        texto += "👤 Cliente: Visitante"

    # Limpeza do carrinho após gerar a mensagem
    request.session['carrinho'] = {}
    request.session.modified = True
    
    texto_final = urllib.parse.quote(texto)
    link_whatsapp = f"https://wa.me/5532984069242?text={texto_final}"
    
    return redirect(link_whatsapp)

# 5. CONTROLES DE QUANTIDADE (No carrinho)
def remover_do_carrinho(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    if id_str in carrinho:
        if carrinho[id_str] > 1:
            carrinho[id_str] -= 1
        else:
            del carrinho[id_str]
    request.session.modified = True
    return redirect('ver_carrinho')

def excluir_item(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    if id_str in carrinho:
        del carrinho[id_str]
    request.session.modified = True
    return redirect('ver_carrinho')