from django.contrib import admin
from .models import Category, Jogo


class ListandoJogos(admin.ModelAdmin):
    list_display = ('id', 'title', 'available')
    search_fields = ('title',)
    list_filter = ('categories',)
    list_editable = ('available',)
    list_per_page = 20

# Register your models here.
admin.site.site_header = 'Jogo-library'
admin.site.register(Category)
admin.site.register(Jogo, ListandoJogos)