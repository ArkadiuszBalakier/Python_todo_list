from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView

from todo.forms import TaskForm
from todo.models import Task, Tag


class IndexView(ListView):
    model = Task
    template_name = 'todo/index.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.prefetch_related('tags').all()


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")

class TagsView(ListView):
    model = Tag

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy('todo:tags')

class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")

class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")
