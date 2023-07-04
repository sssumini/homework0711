from django.db import models

# Create your models here.
class Album(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.TextField(max_length=200)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Track(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, blank=False, null=False, on_delete=models.CASCADE, related_name='tracks')
    number = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)