from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phno=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.email.split('@')[0]