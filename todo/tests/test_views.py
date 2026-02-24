from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from todo.models import Task, Tag


class TaskViewTests(TestCase):
    def test_toggle_task_completed(self):
        task = Task.objects.create(
            content="Test Task",
            is_completed=False,
            deadline=timezone.now(),
        )
        url = reverse("todo:task-toggle", kwargs={"pk": task.id})
        response = self.client.post(url)
        task.refresh_from_db()
        self.assertTrue(task.is_completed)

class TodoViewsTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")
        self.task = Task.objects.create(content="Test Task", is_completed=False)
        self.task.tags.add(self.tag)

    def test_index_view(self):
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/index.html')
        self.assertContains(response, "Test Task")

    def test_task_create_view(self):
        response = self.client.post(reverse('todo:task-create'), {
            'content': 'New Task',
            'tags': [self.tag.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(content='New Task').exists())

    def test_task_delete_view(self):
        url = reverse('todo:task-delete', kwargs={'pk': self.task.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_tags_list_view(self):
        response = self.client.get(reverse('todo:tags'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Urgent")

    def test_tag_create_view(self):
        response = self.client.post(reverse('todo:tag-create'), {'name': 'Work'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(name='Work').exists())