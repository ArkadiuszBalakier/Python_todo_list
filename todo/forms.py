from django import forms

from todo.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_completed", "tags"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                }
            ),
            "deadline": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),
            "is_completed": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-control",
                }
            )
        }