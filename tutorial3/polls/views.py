from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from .models import Question,Choice
from django.template import loader
from django.urls import reverse

def index(request):
    return HttpResponse("This is the index page")

def detail(request,question_id):
    return HttpResponse("These are the details to the question page with question_id" % question_id)

def results(request,question_id):
    return HttpResponse("This is the page that lists the results of the web page %s" % question_id)

def vote(request,question_id):
    return HttpResponse("This is the page where people vote %s" % question_id )

