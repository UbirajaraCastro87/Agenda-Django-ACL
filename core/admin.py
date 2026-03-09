from django.contrib import admin
from core.models import Eventos

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_details_display = ['titulo','data','data_criacao']
    list_filter = ['data_evento','usuario']
    search_fields = ['titulo','descricao']

admin.site.register(Eventos,EventosAdmin)
