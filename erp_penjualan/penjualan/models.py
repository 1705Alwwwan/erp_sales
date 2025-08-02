from django.db import models
from django.contrib.auth.models import User

class Produk(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nama_produk

class Penjualan(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.PositiveIntegerField()
    total_harga = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    kasir = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.total_harga = self.produk.harga * self.jumlah
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produk} - {self.jumlah}"
