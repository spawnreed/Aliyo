from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Board, Response, Phrase, Tag

# Create your views here.


def search_form(request):
    popular = Board.objects.all()
    return render(request, 'search/search_form.html', {'popular': popular})


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        board = Phrase.objects.filter(phrase_title__startswith=q)
        popular = Board.objects.all()
        return render(request, 'search/search_results.html',
                      {'board': board, 'query': q, 'popular': popular})
    else:
        return HttpResponse('Please submit a search term.')


def index(request):
    feed = Board.objects.all()
    return render(request, 'search/index.html', {'feed': feed})


def detail(request, board_id):
        popular = Board.objects.all()
        board = Board.objects.get(pk=board_id)
        board_name = board.board_name
        signs = board.response_set.count()
        response = board.response_set.order_by('board')[0]
        phrase = board.phrase_set.all().filter().order_by('board')[1]
        phrase2 = board.phrase_set.all().filter().order_by('board')[2]
        phrase3 = board.phrase_set.all().filter().order_by('board')[3]
        phrase4 = board.phrase_set.all().filter().order_by('board')[4]
        phrase5 = board.phrase_set.all().filter().order_by('board')[5]



        try:
            board = Board.objects.get(pk=board_id)
        except Board.DoesNotExist:
            raise Http404("Board does not exist")

        return render(request, 'search/board.html', {'board': board, 'popular': popular, 'signs': signs,
                                                     'response': response, 'phrase': phrase, 'board_name': board_name,
                                                     'phrase2': phrase2, 'phrase3': phrase3, 'phrase4': phrase4,
                                                     'phrase5': phrase5})

