from django.urls import reverse
from django.utils import timezone
from django.test import TestCase

from todo.models import Task


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
