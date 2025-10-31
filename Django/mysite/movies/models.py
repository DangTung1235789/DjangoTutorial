from django.db import models

# Create your models here.
class Moviedata(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    duration = models.FloatField()    
    rating = models.FloatField()
    typ = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='pictures/', null=True, blank=True)