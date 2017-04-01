from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CookedAt, Direction, Recipe, Ingredient
from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('recipes')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('recipes')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect('/')
    else:
        return render(request, 'login.html')


@login_required
def form(request):
    if request.method == 'POST':
        frm = BookmarkForm(request.POST)
        if frm.is_valid():
            frm.save()
            return JsonResponse({'status': 'created'})
        else:
            return JsonResponse({'error': frm.errors})
    return render(request, 'form.html')