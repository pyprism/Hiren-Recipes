from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CookedAt, Recipe
from .forms import CookedAtForm, RecipeForm
from django.http import JsonResponse
from django.contrib import auth
from django.contrib import messages
import logging


def login(request):
    """
    Handle authentication
    :param request:
    :return:
    """
    if request.user.is_authenticated:
        return redirect('create')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            # return redirect('recipes')
            return redirect('create')
        else:
            messages.error(request, 'Username/Password is not valid!')
            return redirect('/')
    else:
        return render(request, 'login.html')


@login_required
def create(request):
    if request.method == 'POST':
        logger = logging.getLogger(__name__)
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            # validated_recipe = recipe_form.save(commit=False)
            # validated_direction = direction_form.save(commit=False)
            # validated_ingredient = ingredient_form.save()
            # validated_recipe.ingredient = validated_ingredient
            recipe_form.save()
            print("saved")
            messages.info(request, 'Recipe Added')
            return render(request, 'add.html')
        else:
            messages.error(request, recipe_form.errors)
            print(recipe_form.errors)
            print("errrorrr")
            return render(request, 'add.html')
    return render(request, 'add.html')