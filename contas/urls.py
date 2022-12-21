from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='index'),

    path('registrar/', registrar, name='registrar'),
    path('logar/', logar, name='login'),
    path('logout/', logout, name='logout'),

    path('produto/', produto, name='produto'),
    path('pedidos/', pedidos, name='pedidos'),

    path('cliente/<str:pk>/', cliente, name='cliente'),
    path('criar_cliente/', criarCliente, name='criar_cliente'),
    path('atualizar_cliente/<str:pk>/', atualizarCliente, name='atualizar_cliente'),
    path('excluir_cliente/<str:pk>/', excluirCliente, name='excluir_cliente'),
    
    path('criar_pedido/<str:pk>/', criarPedido, name='criar_pedido'),
    path('atualizar_pedido/<str:pk>/', atualizarPedido, name='atualizar_pedido'),
    path('excluir_pedido/<str:pk>/', excluirPedido, name='excluir_pedido'),
]