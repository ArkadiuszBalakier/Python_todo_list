from django import views
from django.urls import path

from todo.views import IndexView, TagsView, TagDeleteView

app_name = "todo"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("tags/", TagsView.as_view(), name='tags'),
    path("tag/<int:pk>/", TagDeleteView.as_view(), name='tags-delete'),
]