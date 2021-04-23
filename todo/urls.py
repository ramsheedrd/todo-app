
from django.urls import path

from .views import HomeView, create_todo, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path('create/', create_todo),
    path('update/<pk>/', TodoUpdateView.as_view()),
    path('delete/<pk>/', TodoDeleteView.as_view()),
    path('', HomeView.as_view()),

]
