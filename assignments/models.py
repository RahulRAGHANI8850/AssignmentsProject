from django.db import models

# Create your models here.
class assignment(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    msg = models.TextField()
    time = models.DateTimeField(auto_now=True)
    projectFile = models.FileField()

    def __str__(self):
        return self.email