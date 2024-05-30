from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    sujet = models.CharField(max_length=500, null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
