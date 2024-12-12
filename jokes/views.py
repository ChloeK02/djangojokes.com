from django.shortcuts import render

from django.views.generic import ListView

from .models import Joke

from django.views.generic import DetailView, ListView

from django.views.generic import CreateView, DetailView, ListView, UpdateView

class JokeListView(ListView):
    model = Joke

class JokeDetailView(DetailView):
    model = Joke

class JokeCreateView(CreateView):
    model = Joke
    fields = ['question', 'answer']

class JokeUpdateView(UpdateView):
    model = Joke
    fields = ['question', 'answer']