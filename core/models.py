from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class words(models.Model):
    word = models.CharField(max_length=100)
    pronunciation = models.CharField(max_length=150, null=True, blank=True)
    meaning = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    added_by = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.word

class contact_message(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)   
    msg = models.TextField()

    def __str__(self):
        return self.name  