# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding  import python_2_unicode_compatible
from django.db import models


# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date= models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return " %s was published on  %s "%(self.question_text, self.pub_date)

@python_2_unicode_compatible
class Choice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    choice= models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice

