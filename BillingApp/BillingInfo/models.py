from django.db import models
from django.contrib.auth.models import User

class BillInfo(models.Model):
    #owner_name = models.ForeignKey(User)
    bill_content = models.CharField(max_length = 50)
    cost = models.IntegerField()
    bill_release_date = models.DateTimeField()

    class Meta:
        db_table = 'BillInfo'