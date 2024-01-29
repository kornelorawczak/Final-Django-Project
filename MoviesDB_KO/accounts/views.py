from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

def custom_logout(request):
    # Wyloguj użytkownika
    from django.contrib.auth import logout
    logout(request)
    # Przekieruj na stronę logowania
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'accounts/login_success.html')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})