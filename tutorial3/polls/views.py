from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render,get_object_or_404

# Import the render function to directly load,request,template_name, context manager
# Importing the Question class from the models

from django.template import loader
# The django template loader to load the template into the program

def index(request):
   question_list= Question.objects.all()
   context = {"question_list":question_list}
   return render(request,'polls/index.html',context)

def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    context = {"question":question}
    return render(request,'polls/detail.html',context)

def results(request,question_id):
    return HttpResponse("This is the page that lists the results of the web page %s" % question_id)

def vote(request,question_id):
    return HttpResponse("This is the page where people vote %s" % question_id )

