from django.forms import ModelForm
from .models import Recipe, Ingredient, CookedAt, Direction


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ('ingredient', 'direction')


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CookedAtForm(ModelForm):
    class Meta:
        model = CookedAt
        exclude = 'recipe'


class DirectionForm(ModelForm):
    class Meta:
        model = Direction
        fields = "__all__"
