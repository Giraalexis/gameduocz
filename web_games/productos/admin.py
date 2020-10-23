from django.contrib import admin

# Register your models here.
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

#registrta modelo para ser administrado
admin.site.register(Producto,ProductoAdmin)