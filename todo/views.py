from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from todo.models import Task, Tag


class IndexView(ListView):
    model = Task
    template_name = 'todo/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.prefetch_related('tags').all()


class TagsView(ListView):
    model = Tag