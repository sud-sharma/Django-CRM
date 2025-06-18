from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record
from .forms import RecordModelForm


# def home(request):
#     return render(request, 'home.html')


def home(request):
    records = Record.objects.all().order_by('-created_at')[:10]  # Fetch the latest 10 records


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
        return render(request, 'home.html', {'records': records})
    

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful! You are now logged in.')
                return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})

def customer_record(request, record_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to view records.')
        return redirect('home')
    try:
        record = Record.objects.get(id=record_id)
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')
        return redirect('home')

    return render(request, 'customer_record.html', {'record': record})
    
def delete_record(request, record_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to delete records.')
        return redirect('home')
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete records.')
        return redirect('home')
    if request.method != 'POST':
        messages.error(request, 'Invalid request method.')
        return redirect('home')
    try:
        record = Record.objects.get(id=record_id)
        record.delete()
        messages.success(request, 'Record deleted successfully.')
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')

    return redirect('home')

def add_record(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to add records.')
        return redirect('add_record')
    
    if request.method == 'POST':
        form = RecordModelForm(request.POST)
        if form.is_valid():
            record = Record(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pin_code=form.cleaned_data['pin_code']
            )
            record.save()
            messages.success(request, 'Record added successfully!')
            return redirect('home')
    else:
        form = RecordModelForm()

    return render(request, 'add_record.html', {'form': form})

def update_record(request, record_id):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to update records.')
        return redirect('home')
    
    try:
        record = Record.objects.get(id=record_id)
    except Record.DoesNotExist:
        messages.error(request, 'Record not found.')
        return redirect('home')

    if request.method == 'POST':
        form = RecordModelForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect('customer_record', record_id=record.id)
    else:
        form = RecordModelForm(request.POST or None,  instance=record)

    return render(request, 'edit_record.html', {'form': form, 'record': record})
        