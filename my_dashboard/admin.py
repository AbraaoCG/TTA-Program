from django.contrib import admin
from .models import StockSymbol

@admin.register(StockSymbol)
class StockSymbolAdmin(admin.ModelAdmin):
    list_display = ('symbol',)
    search_fields = ('symbol',)
    list_filter = ('symbol',)