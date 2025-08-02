from django import forms
from .models import Penjualan

class PenjualanForm(forms.ModelForm):
    class Meta:
        model = Penjualan
        fields = ['produk', 'jumlah']
