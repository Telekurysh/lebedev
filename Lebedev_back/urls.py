# movies/urls.py
from django.urls import path
from .views import MovieListCreateAPIView, MovieSearchAPIView

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    # path('movies/search/', MovieSearchAPIView.as_view(), name='movie-search'),
]
