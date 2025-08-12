from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title

    # bu aynan shu sahifaga qaytarish uchun
    def get_absolute_url(self):
        return reverse("detail_view", args=[str(self.pk)])
