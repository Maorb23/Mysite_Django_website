from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages import get_messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.



def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('main_index')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('Maor_proj.userlogin:login')  # Use the full namespace

    return render(request, 'userlogin/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('main_index')








def test_messages(request):
    messages.success(request, "This is a success message!")
    messages.error(request, "This is an error message!")
    messages.info(request, "This is an info message!")
    return render(request, 'userlogin/login.html')


def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered!")
            return redirect('main_index')
        else:
            messages.error(request, "There was an error. Please try again.")
            return redirect('Maor_proj.userlogin:register')
    else:
        form = UserCreationForm()
    return render(request, 'userlogin/register.html', {'form': form})