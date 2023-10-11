from rest_framework import generics
from .models import Genre
from .serializers import GenreSerializer
from .models import Director
from .serializers import DirectorSerializer

from rest_framework import generics
from django.db.models import Q
from .models import Movie
from .serializers import MovieSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated 

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer



class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    queryset = Movie.objects.all()


class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Применяем IsAuthenticated

    def get_queryset(self):
        queryset = Movie.objects.all()
        genre_id = self.request.query_params.get('genre', None)
        director_id = self.request.query_params.get('director', None)

        if genre_id:
            queryset = queryset.filter(genres__id=genre_id)
        if director_id:
            queryset = queryset.filter(director__id=director_id)

        return queryset
