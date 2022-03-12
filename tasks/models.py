from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Task(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    estimated_time = models.IntegerField()
    details = models.TextField()
    reserved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_date_created(self):
        return str(datetime.now().day - self.created_at.day)


class Reserve(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}, {self.task.title}'
