from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class shorturl(models.Model):
    original_url = models.URLField(blank=False)
    short_query = models.CharField(blank=False, max_length=8)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Issues(models.Model):
    issueId = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    query = models.CharField(max_length=100)

    def __str__(self):
        return self.subject
    