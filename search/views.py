from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Response, Phrase, Tag

# Create your views here.


def search_form(request):
    popular = Board.objects.all()
    return render(request, 'search/search_form.html', {'popular': popular})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        board = Phrase.objects.filter(response__response_text__startswith=q)
        return render(request, 'search/search_results.html',
                      {'board': board, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
