from django.forms import ModelForm
from .models import Recipe, CookedAt


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"


class CookedAtForm(ModelForm):
    class Meta:
        model = CookedAt
        exclude = ('recipe',)

