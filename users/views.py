from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso. Faça login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    form_errors = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email:
            form_errors['email'] = 'Informe o email.'
        if not password:
            form_errors['password'] = 'Informe a senha.'

        if email and password:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('tasks:task_list')
            else:
                form_errors['non_field_errors'] = 'Credenciais inválidas. Tente novamente.'

    return render(request, 'login.html', {'form_errors': form_errors})


def logout_view(request):
    logout(request)
    return redirect('home')  # Redireciona para /
