from django.db import models
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
