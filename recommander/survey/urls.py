from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('favorite',views.favorite_movie,name='favorite'),
    path('watched',views.watched_movies,name='watched'),
    path('recommendations',views.recommended_movies,name='recommendations'),
]