from django import views
from django.urls import path

from todo.views import IndexView, TagsView, TagDeleteView, TagUpdateView, TagCreateView

app_name = "todo"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("tags/", TagsView.as_view(), name='tags'),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name='tags-delete'),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name='tags-update'),
    path("tag/create/", TagCreateView.as_view(), name='tags-create'),
]