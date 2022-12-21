from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200, null=True)
    telefone = models.CharField(max_length=200, null=True, unique=True)
    email = models.CharField(max_length=200, null=True)
    data_criacao = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    CATEGORIA = (
        ('Interior', 'Interior'),
        ('Ar livre', 'Ar livre'),
    )

    nome = models.CharField(max_length=200, null=True)
    preco = models.FloatField(null=True)
    categoria = models.CharField(max_length=200, choices=CATEGORIA)
    descricao = models.CharField(max_length=300, null=True, blank=True)
    data_criacao = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS = (
        ('Pendente', 'Pendente'),
        ('Pedido a caminho', 'Pedido a caminho'),
        ('Entregue', 'Entregue'),
    )

    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, null=True, on_delete=models.SET_NULL)
    data_criacao = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.produto.nome
    

