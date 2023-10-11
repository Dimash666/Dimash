from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreList.as_view(), name='genre-list'),
    path('directors/', views.DirectorList.as_view(), name='director-list'),
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>',views.MovieDetail.as_view(),name='movie-detail')
]
