from django.db import models

# Create your models here.
class Tweet(models.Model):
    tw_text = models.CharField(max_length=200)
    tw_user = models.CharField(max_length=200)
    tw_cat = models.FloatField(max_length=200)