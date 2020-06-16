from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404

from .models import Question

def home_page(request):
    return render (request, 'lists/home.html', {
        'new_item_text': request.POST.get('item_text',''),
    })

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'lists/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)