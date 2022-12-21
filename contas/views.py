from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import PedidoForm, ClienteForm
from .filters import PedidoFiltro
from .forms import CriarUsuarioForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout


def registrar(request):
    form = CriarUsuarioForm()

    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para o usuário {usuario}')
            return redirect('login')

    context = {'form':form}
    return render(request, 'contas/registrar.html', context)


def logar(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.info(request, 'Usuário ou senha incorretos')

    context = {}
    return render(request, 'contas/logar.html', context)


def logout(request):    
    django_logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()

    ultimos_cinco_pedidos = pedidos.order_by('-id')[:5]

    total_clientes = clientes.count()
    entregues = pedidos.filter(status='Entregue').count()
    pendentes = pedidos.filter(status='Pendente').count()
    total_pedidos = pedidos.count()
    
    pedidos_entregues = pedidos.filter(status='Entregue').reverse()
    cinco_ultimos_entregues = pedidos_entregues.order_by('data_criacao')[:5]
    
    
    context = {'pedidos':pedidos, 'clientes':clientes, 'entregues':entregues, 'pendentes':pendentes, 'total_pedidos':total_pedidos, 'total_clientes':total_clientes, 'ultimos_cinco_pedidos':ultimos_cinco_pedidos, 'cinco_ultimos_entregues':cinco_ultimos_entregues}
    return render(request, 'contas/dashboard.html', context)


@login_required(login_url='login')
def pedidos(request):
    pedidos = Pedido.objects.all()

    context = {'pedidos':pedidos}
    return render(request, 'contas/pedidos.html', context)
    

@login_required(login_url='login')
def produto(request):
    produtos = Produto.objects.all()

    context = {'produtos':produtos}
    return render(request, 'contas/produtos.html', context)


@login_required(login_url='login')
def cliente(request, pk):
    clientes = Cliente.objects.get(id=pk)

    pedidos = clientes.pedido_set.all()

    total_pedidos_cliente = pedidos.count()
    

    meuFiltro = PedidoFiltro(request.GET, queryset=pedidos)
    pedidos = meuFiltro.qs

    context = {'pedidos':pedidos, 'clientes':clientes, 'total_pedidos_cliente':total_pedidos_cliente, 'meuFiltro':meuFiltro}
    return render(request, 'contas/cliente.html', context)


@login_required(login_url='login')
def criarPedido(request, pk):
    PedidoFormSet = inlineformset_factory(Cliente, Pedido, fields=('produto','status'), extra=5)
    cliente = Cliente.objects.get(id=pk)
    formset = PedidoFormSet(queryset=Pedido.objects.none(), instance=cliente)

    if request.method == 'POST':
        formset = PedidoFormSet(request.POST, instance=cliente)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'contas/pedido_form.html', context)


@login_required(login_url='login')
def atualizarPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)
    formset = PedidoForm(instance=pedido)

    if request.method == 'POST':
        formset = PedidoForm(request.POST, instance=pedido)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'contas/pedido_form.html', context)


@login_required(login_url='login')
def excluirPedido(request, pk):
    pedido = Pedido.objects.get(id=pk)

    if request.method == 'POST':
        pedido.delete()
        return redirect('/')
    else:
        context = {'pedido':pedido}
        return render(request, 'contas/confirmar_exclusao.html', context)


@login_required(login_url='login')
def criarCliente(request):
    form_cliente = ClienteForm()

    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('/')

    context = {'form_cliente':form_cliente}
    return render(request, 'contas/cliente_form.html', context)


@login_required(login_url='login')
def atualizarCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)
    form_cliente = ClienteForm(instance=cliente)

    if request.method == 'POST':
        form_cliente = ClienteForm(request.POST, instance=cliente)
        if form_cliente.is_valid():
            form_cliente.save()
            return redirect('/')

    context = {'form_cliente':form_cliente}
    return render(request, 'contas/cliente_form.html', context)


def excluirCliente(request, pk):
    cliente = Cliente.objects.get(id=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('/')
    else:
        context = {'cliente':cliente}
        return render(request, 'contas/confirmar_exclusao_cliente.html', context)


