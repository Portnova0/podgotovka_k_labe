from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe
class RecipeList(ListView):
    model = Recipe
    template_name = 'cooking/cooking.html'
    context_object_name = 'recipes'
# Create your views here.
