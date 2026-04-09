from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('adicionar/<int:doce_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:doce_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('excluir/<int:doce_id>/', views.excluir_item, name='excluir_item'),
    path('finalizar/', views.finalizar_pedido, name='finalizar_pedido'),
]