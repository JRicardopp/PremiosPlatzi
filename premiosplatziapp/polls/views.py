from urllib.parse import quote_from_bytes
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect # es una clase que permite ejecutar un respuesta http 
from django.urls import reverse

from .models import Question, Choice




def vote(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html",{
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))