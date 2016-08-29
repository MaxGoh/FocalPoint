from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
