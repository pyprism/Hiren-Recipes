from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Recipe(models.Model):
    name = models.CharField(max_length=800, unique=True)
    image = models.ImageField(upload_to='hiren')
    image_thumbnail = ImageSpecField(source='hiren',
                                     processors=[ResizeToFill(363, 241)],
                                     format='JPEG',
                                     options={'quality': 60})

    preparation_time = models.FloatField(null=True, blank=True)
    cooking_time = models.FloatField(null=True, blank=True)
    cuisine_type = (
        ('Ame', 'American'),
        ('Chi', 'Chinese'),
        ('Ind', 'Indian'),
        ('Ita', 'Italian'),
        ('Fre', 'French'),
        ('Gre', 'Greek'),
        ('Med', 'Mediterranean'),
        ('Mex', 'Mexican'),
        ('Nor', 'Nordic'),
        ('Tur', 'Turkish'),
        ('Ban', 'Bangladesh'),
        ('Oth', 'Other'),
    )
    cuisine = models.CharField(max_length=3, choices=cuisine_type, default='Oth')
    meal_type = (
        ('Mai', 'Main Course'),
        ('Sna', 'Snacks'),
        ('Bre', 'Breakfast'),
        ('Sid', 'Side Dished'),
        ('Des', 'Dessert'),
        ('Cak', 'Caking and Baking'),
        ('Dri', 'Drinks'),
        ('Oth', 'Other')
    )
    meal = models.CharField(max_length=3, choices=meal_type, default='Oth')
    video = models.URLField(null=True, blank=True)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=800)
    amount = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CookedAt(models.Model):
    date = models.DateTimeField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Direction(models.Model):
    step = models.IntegerField()
    timer = models.TimeField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)