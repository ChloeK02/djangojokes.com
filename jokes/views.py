from django.shortcuts import render

from django.views.generic import ListView

from .models import Joke

from django.views.generic import DetailView, ListView

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke