# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DeleteView):
    template_name = 'polls/detail.html'
    model = Question

# Create your views here.


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'




def vote(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',
                      {'question':question,
                       'error_message':"You didn't select a choice"})
    else:
        selected_choice.vote+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
