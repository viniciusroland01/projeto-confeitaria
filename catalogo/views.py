from django.shortcuts import render, get_object_or_404, redirect
from .models import Doce
import urllib.parse

def home(request):
    doces = Doce.objects.all()
    return render(request, 'catalogo/home.html', {'doces': doces})

def adicionar_ao_carrinho(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    
    # Se vier da Home (POST), pega a quantidade digitada. Se vier do botão '+' no carrinho, adiciona 1.
    quantidade = 1
    if request.method == 'POST':
        quantidade = int(request.POST.get('quantidade', 1))
        
    carrinho[id_str] = carrinho.get(id_str, 0) + quantidade
    request.session['carrinho'] = carrinho
    request.session.modified = True
    
    # Redirecionamento inteligente
    referencia = request.META.get('HTTP_REFERER', '')
    if 'carrinho' in referencia:
        return redirect('ver_carrinho')
    return redirect('home')

def remover_do_carrinho(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    if id_str in carrinho:
        if carrinho[id_str] > 1:
            carrinho[id_str] -= 1
        else:
            del carrinho[id_str]
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('ver_carrinho')

def excluir_item(request, doce_id):
    carrinho = request.session.get('carrinho', {})
    id_str = str(doce_id)
    if id_str in carrinho:
        del carrinho[id_str]
    request.session['carrinho'] = carrinho
    request.session.modified = True
    return redirect('ver_carrinho')

def ver_carrinho(request):
    carrinho_sessao = request.session.get('carrinho', {})
    itens_carrinho = []
    total_geral = 0
    for doce_id, quantidade in carrinho_sessao.items():
        doce = get_object_or_404(Doce, id=doce_id)
        subtotal = doce.preco * quantidade
        total_geral += subtotal
        itens_carrinho.append({'doce': doce, 'quantidade': quantidade, 'subtotal': subtotal})
    return render(request, 'catalogo/carrinho.html', {'itens': itens_carrinho, 'total': total_geral})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Doce
import urllib.parse

# ... (mantenha as outras views como home e adicionar_ao_carrinho)

def finalizar_pedido(request):
    carrinho_sessao = request.session.get('carrinho', {})
    
    if not carrinho_sessao:
        return redirect('home')
    
    # 1. Início da mensagem
    texto = "🍰 *NOVO PEDIDO - FERNANDA DOCES* 🍰\n\n"
    total = 0
    itens_formatados = ""

    # 2. Processando os itens com segurança
    for doce_id, qtd in carrinho_sessao.items():
        try:
            doce = Doce.objects.get(id=doce_id)
            subtotal = doce.preco * qtd
            total += subtotal
            itens_formatados += f"▪️ {qtd}x {doce.nome} - R$ {subtotal:.2f}\n"
        except Doce.DoesNotExist:
            continue # Se o doce foi deletado do banco, pula ele

    texto += itens_formatados
    texto += f"\n💰 *TOTAL DO PEDIDO: R$ {total:.2f}*"
    texto += f"\n--------------------------\n"

    # 3. Lógica de Fidelidade (Melhorada para evitar o erro que você viu)
    if request.user.is_authenticated:
        texto += f"👤 *Cliente:* {request.user.username}\n"
        
        # Tentamos pegar o perfil, se não existir, criamos um na hora ou ignoramos
        try:
            # Calcula pontos (ex: 1 ponto a cada 10 reais)
            pontos_ganhos = int(total // 10) 
            
            # Tenta acessar o perfil. O 'hasattr' evita o erro que trava a mensagem
            if hasattr(request.user, 'perfil'):
                perfil = request.user.perfil
                perfil.pontos += pontos_ganhos
                perfil.save()
                texto += f"✨ *Fidelidade:* Você acumulou +{pontos_ganhos} pontos!\n"
                texto += f"📊 *Saldo Atual:* {perfil.pontos} pts"
            else:
                texto += f"✨ *Fidelidade:* Você ganhou {pontos_ganhos} pontos nesta compra!"
        except Exception as e:
            # Se der qualquer erro nos pontos, a mensagem não "morre"
            print(f"Erro ao processar pontos: {e}") 
    else:
        texto += "👤 *Cliente:* Visitante (faça login para ganhar pontos!)"

    # 4. Limpeza do carrinho e redirecionamento
    request.session['carrinho'] = {}
    request.session.modified = True
    
    # Codificação correta para URL (essencial para o WhatsApp ler os emojis)
    texto_final = urllib.parse.quote(texto)
    link_whatsapp = f"https://api.whatsapp.com/send?phone=5532984069242&text={texto_final}"
    
    return redirect(link_whatsapp)