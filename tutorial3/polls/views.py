from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from .models import Question,Choice
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

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
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/results.html',{"question":question})


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # return it to display form
        context= {"question":question,
                  "error_message":"You didn't select a choice",}
        return render(request,'polls/detail.html',context)
    else:
        selected_choice.vote +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



