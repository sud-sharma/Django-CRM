from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# def home(request):
#     return render(request, 'home.html')


def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.', extra_tags='danger')
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = user.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('home')
        else:
            messages.error(request, 'Passwords do not match.', extra_tags='danger')
            return redirect('home')
    else:
        return render(request, 'register.html', {})
