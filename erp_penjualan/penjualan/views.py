from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PenjualanForm
from .models import Penjualan
from django.utils import timezone
from datetime import timedelta

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat. Silakan login.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())

    total_harian = Penjualan.objects.filter(tanggal=today).count()
    total_mingguan = Penjualan.objects.filter(tanggal__gte=start_of_week).count()

    return render(request, 'dashboard.html', {
        'total_harian': total_harian,
        'total_mingguan': total_mingguan
    })

@login_required
def transaksi(request):
    if request.method == 'POST':
        form = PenjualanForm(request.POST)
        if form.is_valid():
            penjualan = form.save(commit=False)
            penjualan.kasir = request.user
            penjualan.save()
            return redirect('transaksi')
    else:
        form = PenjualanForm()

    data = Penjualan.objects.all().order_by('-tanggal')
    return render(request, 'transaksi.html', {'form': form, 'data': data})
