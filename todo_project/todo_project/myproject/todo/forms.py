from django import forms
from .models import Task
from django.core.exceptions import ValidationError
from django.utils import timezone

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'completed', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите название задачи',
                'class': 'form-control'
            }),
            'completed': forms.CheckboxInput(),
            'due_date': forms.DateInput(attrs={
                'class': 'datepicker form-control',
                'placeholder': 'Выберите дату',
                'type': 'date'  # Убедитесь, что это совместимо с вашим интерфейсом
            }),
        }

    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise ValidationError('Дата выполнения не может быть в прошлом.')
        return due_date

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise ValidationError('Название задачи обязательно для заполнения.')
        return title