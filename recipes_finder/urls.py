from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='recipe-finder-home'),
    path('about/', views.about, name='recipe-finder-about'),
]