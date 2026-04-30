from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    """Learning Topic"""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']
        db_table = 'topic'

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Entry of a Topic"""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date_added']
        db_table = 'entry'

    def __str__(self):
        if len(self.text) <= 50:
            return self.text
        else:
            return self.text[:47] + '...'
