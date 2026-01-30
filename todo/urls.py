from django import views
from django.urls import path

from todo.views import IndexView, TagsView, TagDeleteView, TagUpdateView, TagCreateView, TaskCreateView, \
    ToggleTaskCompleteView, TaskUpdateView, TaskDeleteView

app_name = "todo"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("tags/", TagsView.as_view(), name='tags'),
    path("task/create/", TaskCreateView.as_view(), name='task-create'),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name='task-update'),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name='task-delete'),
    path("task/<int:pk>/toggle", ToggleTaskCompleteView.as_view(), name='task-toggle'),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name='tags-delete'),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name='tags-update'),
    path("tag/create/", TagCreateView.as_view(), name='tags-create'),
]