from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from .models import Movies


def index(request):
    # get the state of browser, i.e where the user left off last time
    # 3 possible values: 1, 2, 3
    # 1: favorite movie
    # 2: few more movies to make the classification stronger
    # 3: Survey complete, user can track recommendations and/or keep adding new movies to watch list

    survey_stage = request.session.get('survey_stage',1)

    if survey_stage == 1:
        return redirect('favorite')
    elif survey_stage == 2:
        return redirect('watched')
    elif survey_stage == 3:
        return redirect('recommendations')

def favorite_movie(request):
    survey_stage = request.session.get('survey_stage', 1)
    if survey_stage != 1:
        return redirect('index')
    
    top_movies = Movies.objects.all().order_by('-vote_count','-vote_average')[:10]
    return render(request, 'survey/favorite.html',context={'movies':top_movies})

def watched_movies(request):
    survey_stage = request.session.get('survey_stage', 1)
    
    if survey_stage != 2:
        return redirect('index')

    return HttpResponse('At Survey Stage 2: Watched movies')
    
def recommended_movies(request):
    survey_stage = request.session.get('survey_stage', 1)
    if survey_stage != 3:
        return redirect('index')

    return HttpResponse('At Survey Stage 3: Recommended movies')