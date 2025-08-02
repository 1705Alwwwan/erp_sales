from django.contrib import admin
from .models import Produk, Penjualan

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_produk', 'harga')
    search_fields = ('nama_produk',)
    list_per_page = 20

@admin.register(Penjualan)
class PenjualanAdmin(admin.ModelAdmin):
    list_display = ('id', 'tanggal', 'produk', 'jumlah', 'total_harga', 'kasir')
    list_filter = ('tanggal', 'produk', 'kasir')
    search_fields = ('produk__nama_produk', 'kasir__username')
    date_hierarchy = 'tanggal'
    list_per_page = 20
