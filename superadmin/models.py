from django.db import models

# Create your models here.
from django.db import models

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='carousels/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Complaint(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
