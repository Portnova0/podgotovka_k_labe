from django.urls import path
from .views import RecipeList
urlpatterns = [

    path('cooking/', RecipeList.as_view(), name='index'),
]
