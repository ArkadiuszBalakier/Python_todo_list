from django.test import TestCase
from django.utils import timezone
from todo.models import Task, Tag
from datetime import timedelta

class TodoModelsTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")

    def test_tag_str(self):
        self.assertEqual(str(self.tag), "Urgent")

    def test_task_creation_and_fields(self):
        deadline = timezone.now() + timedelta(days=1)
        task = Task.objects.create(
            content="Finish the project",
            deadline=deadline
        )
        task.tags.add(self.tag)

        self.assertEqual(task.content, "Finish the project")
        self.assertFalse(task.is_completed)
        self.assertEqual(task.tags.count(), 1)
        self.assertIn(self.tag, task.tags.all())

    def test_task_related_name(self):
        task = Task.objects.create(
            content="Linked Task",
            deadline=timezone.now()
        )
        task.tags.add(self.tag)
        self.assertEqual(self.tag.tasks.count(), 1)
        self.assertEqual(self.tag.tasks.first().content, "Linked Task")

    def test_task_ordering(self):
        now = timezone.now()

        task1 = Task.objects.create(
            content="Old Completed",
            deadline=now,
            is_completed=True
        )
        task2 = Task.objects.create(
            content="Old Pending",
            deadline=now,
            is_completed=False
        )
        task3 = Task.objects.create(
            content="New Pending",
            deadline=now,
            is_completed=False
        )

        tasks = Task.objects.all()
        self.assertEqual(tasks[0], task3)
        self.assertEqual(tasks[1], task2)
        self.assertEqual(tasks[2], task1)