from django.db import models

# Create your models here.


class Phone(models.Model):
    title=models.CharField(max_length=150,unique=True)
    model=models.CharField(max_length=40)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

