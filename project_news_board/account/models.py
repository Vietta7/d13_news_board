from django.contrib.auth.models import User
from django.db import models


class Code(models.Model):
    code = models.IntegerField()
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
