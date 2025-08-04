from django.contrib import admin
from .models import Contato

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'created_at')
    search_fields = ('nome', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)