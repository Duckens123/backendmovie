from django.urls import path
from movies import views

urlpatterns=[
    path('acteurs/', views.acteur_list, name='acteur_list'),
    path('acteurs/<int:pk>/', views.acteur_detail, name='acteur_detail'),
    path('acteurs/create/', views.acteur_create, name='acteur_create'),

    path('films/', views.film_list, name='film_list'),
    path('films/<int:pk>/', views.film_detail, name='film_detail'),
    path('films/create/', views.film_create, name='film_create'),

    path('realisateurs/', views.realisateur_list, name='realisateur_list'),
    path('realisateurs/<int:pk>/', views.realisateur_detail, name='realisateur_detail'),
    path('realisateurs/create/', views.realisateur_create, name='realisateur_create'),

    path('avis/', views.avis_list, name='avis_list'),
    path('avis/<int:pk>/', views.avis_detail, name='avis_detail'),
    path('avis/create/', views.avis_create, name='avis_create'),
]