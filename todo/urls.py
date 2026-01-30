from django import views
from django.urls import path

from todo.views import IndexView

app_name = "todo"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]