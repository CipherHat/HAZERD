from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)