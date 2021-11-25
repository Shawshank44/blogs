from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateField(auto_now=True)
