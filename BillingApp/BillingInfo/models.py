from django.db import models
from django.contrib.auth.models import User

class BillInfo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    amount = models.IntegerField()
    event_time = models.DateTimeField()
