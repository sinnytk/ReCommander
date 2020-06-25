from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
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

    if request.POST:
        selected_movie = request.POST.get('selected_movie')
        if selected_movie:
            watched = [selected_movie]
            request.session['watched'] = watched
            request.session['survey_stage'] = 2
            return redirect('watched')

    survey_stage = request.session.get('survey_stage', 1)
    if survey_stage != 1:
        return redirect('index')
    
    top_movies = Movies.objects.all().order_by('-vote_count','-vote_average')[:10]
    return render(request, 'survey/favorite.html',context={'movies':top_movies})

def watched_movies(request):
    survey_stage = request.session.get('survey_stage', 1)
    
    if survey_stage != 2:
        return redirect('index')
    
    selected_movie = request.session.get('watched')[0]
    print(selected_movie)
    selected_movie = Movies.objects.get(id=selected_movie)    
    similar_movies = Movies.objects.all().order_by('-vote_count','-vote_average')[:10]
    return render(request, 'survey/watched.html',
        context={'movies':similar_movies,'selected_movie':selected_movie})
    
def recommended_movies(request):
    survey_stage = request.session.get('survey_stage', 1)
    if survey_stage != 3:
        return redirect('index')

    return HttpResponse('At Survey Stage 3: Recommended movies')

def search_movies(request):
    if request.is_ajax():
        query = request.GET.get('query',None)
        if query and len(query)>0:
            movies = Movies.objects.filter(title__icontains=query)[:10]
        else:
            movies = []
        html = render_to_string(
            template_name="survey/movies.html",
            context={'movies':movies}
        )
        return JsonResponse(data={'html_from_view':html},safe=False)
    else:
        return JsonResponse(data={'success':False})

def add_movie(request):
    if request.POST:
        movie = request.POST.get('movie')
        if not movie:
            return JsonResponse(data={'success':False,'message':'No such movie found'})
        watched = request.session.get('watched')
        print('Movie to add: ', movie)
        if not watched:
            watched = []
        print('Previous watched:', watched)
        watched.append(movie)
        request.session['watched'] = watched