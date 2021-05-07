from django.db import models

# Create your models here.


class Users(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        return self.Email
