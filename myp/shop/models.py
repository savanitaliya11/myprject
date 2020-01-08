from django.db import models


# Create your models here.


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    select = models.CharField(max_length=30)
    message = models.CharField(max_length=30)

    class Meta:
        db_table = 'student'
