from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"



class County(models.Model):
    name = models.CharField(max_length=100, unique=True)
    county = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
