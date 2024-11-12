from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, unique=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)  # Новое поле для даты выполнения

    class Meta:
        ordering = ['due_date', 'created_at']

    def toggle_completion(self):
        self.completed = not self.completed
        self.save()

    def __str__(self):
        return self.title