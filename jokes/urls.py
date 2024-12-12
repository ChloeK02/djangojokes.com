from django.urls import path

from .views import JokeListView

from .views import JokeDetailView, JokeListView

from .views import (
    JokeCreateView, JokeDetailView, JokeListView, JokeUpdateView
)

app_name = 'jokes'
urlpatterns = [
    path('', JokeListView.as_view(), name='list'),
    path('joke/<int:pk>/', JokeDetailView.as_view(), name='detail'),
    path('joke/<int:pk>/update/', JokeUpdateView.as_view(), name='update'),
    path('joke/create/', JokeCreateView.as_view(), name='create'),
]

