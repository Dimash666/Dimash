import django_filters as df
from .models import Movie


class MovieFilter(df.FilterSet):
    genre = df.NumberFilter(field_name='genres__id')
    director = df.NumberFilter(field_name='director__id')

    class Meta:
        models = Movie
        fields = ['genre','director']

