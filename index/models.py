from django.contrib.auth.models import User
from django.db import models


class Role(models.Model):
    role = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.role)

    def get_role(self):
        if self.role == 1:
            return "کارگزار"
        else:
            return "پیمانکار"
