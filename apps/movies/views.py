from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Movie, Genre, Director
from .serializers import MovieSerializer, GenreSerializer, DirectorSerializer
from .permissions import IsOwnerOrReadOnly
from .filters import MovieFilter


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
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = MovieFilter
    search_fields = ['title','description','year']
    


    # def get_queryset(self):
    #     queryset = Movie.objects.all()
    #     genre_id = self.request.query_params.get('genre', None)
    #     director_id = self.request.query_params.get('director', None)

    #     if genre_id:
    #         queryset = queryset.filter(genres__id=genre_id)
    #     if director_id:
    #         queryset = queryset.filter(director__id=director_id)

    #     return queryset

