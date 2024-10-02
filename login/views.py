from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # 원하는 리디렉션 URL로 변경
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form': form})