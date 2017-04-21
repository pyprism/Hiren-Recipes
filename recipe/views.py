from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CookedAt, Recipe
from .forms import CookedAtForm, RecipeForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
        return render(request, 'login.html', {'title': 'Login'})


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
    return render(request, 'add.html', {'title': 'Create New Recipe'})


@login_required
def recipes(request):
    """
    Return all recipe with pagination support
    :param request:
    :return:
    """
    recipes = Recipe.objects.order_by('-id')
    paginator = Paginator(recipes, 8)
    page = request.GET.get('page')
    try:
        yummy = paginator.page(page)
    except PageNotAnInteger:
        # If yummy is not an integer, deliver first page.
        yummy = paginator.page(1)
    except EmptyPage:
        yummy = paginator.page(paginator.num_pages)
    return render(request, 'recipes.html', {"recipes": yummy, 'title': 'Recipes'})


@login_required
def recipe(request, pk=None):
    """
    Serve recipe
    :param request: 
    :param pk: 
    :return: 
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe:
        counter = CookedAt.objects.filter(recipe=recipe).count()
    return render(request, 'recipe.html', {'recipe': recipe, 'title': recipe.name, 'counter': counter})


@login_required
def recipe_edit(request, pk=None):
    """
    Update recipe
    :param request: 
    :param pk: 
    :return: 
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.info(request, "Recipe updated!")
            return redirect('/recipes/' + pk + '/')
        else:
            messages.error(request, form.errors)
            return redirect('/recipes/' + pk + '/')
    return render(request, 'recipe_edit.html', {'recipe': recipe, 'title': recipe.name})


@login_required
def cooked(request, pk=None):
    pass


@login_required
def delete(request, pk=None):
    # try:
    #     Recipe.objects.filter(pk=pk).delete()
    #     messages.info(request, "Recipe Deleted!")
    # except Exception as e:
    #     messages.error(request, e.message)
    Recipe.objects.filter(pk=pk).delete()
    messages.info(request, "Recipe Deleted!")
    return redirect(recipes)


@login_required
def meal(request, meal=None):
    """
    Serve meal by type
    :param request: 
    :param meal: 
    :return: 
    """
    hiren = Recipe.objects.filter(meal=meal)
    return render(request, 'recipes.html', {"recipes": hiren, 'title': 'Recipes'})


@login_required
def cuisine(request, cuisine=None):
    """
    Serve cuisine by type
    :param request: 
    :param cuisine: 
    :return: 
    """
    hiren = Recipe.objects.filter(meal=cuisine)  # get cuisine full name
    return render(request, 'recipes.html', {"recipes": hiren, 'title': 'Recipes'})
