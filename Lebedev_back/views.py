from django.db.models import Q
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from django.shortcuts import redirect


def redirect_to_movies(request):
    return redirect('/api/movies/')


class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieSearchAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        query = self.request.query_params.get('query', None)
        if query is not None:
            search_fields = ['nativeId', 'nativeName', 'director', 'producer']

            search_query = Q()
            for field in search_fields:
                search_query |= Q(**{f"{field}__icontains": query})

            queryset = Movie.objects.filter(search_query)
            return queryset
        else:
            return Movie.objects.all()
