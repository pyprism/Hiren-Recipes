from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CookedAt, Recipe
from .forms import CookedAtForm, RecipeForm
from django.http import JsonResponse
from django.contrib import auth
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging


def login(request):
    """
    Handles authentication
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
    """
    Recipe creation
    :param request:
    :return:
    """
    if request.method == 'POST':
        logger = logging.getLogger(__name__)
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            # validated_recipe = recipe_form.save(commit=False)
            # validated_direction = direction_form.save(commit=False)
            # validated_ingredient = ingredient_form.save()
            # validated_recipe.ingredient = validated_ingredient
            recipe_form.save()
            messages.info(request, 'Recipe Added')
            return redirect('create')
        else:
            messages.error(request, recipe_form.errors)
            logger.info(recipe_form.errors)
            return render(request, 'add.html')
    return render(request, 'add.html')


@login_required
def recipes(request):
    recipes = Recipe.objects.all('-id')
    paginator = Paginator(recipes, 10)
    page = request.GET.get('page')
    try:
        yummy = paginator.page(page)
    except PageNotAnInteger:
        # If yummy is not an integer, deliver first page.
        yummy = paginator.page(1)
    except EmptyPage:
        yummy = paginator.page(paginator.num_pages)
    return render(request, 'recipes.html', {"recipes": yummy})