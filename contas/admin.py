from django.contrib import admin
from .models import Cliente, Produto, Tag, Pedido

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Tag)
admin.site.register(Pedido)
