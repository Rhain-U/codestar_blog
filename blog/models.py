from django.db import models

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
related_name = "comments")
    author = models.ForeignKey(
        User, on_delete = models.CASCADE,
related_name = "commenter")
    body = models.TextField()
    approved = models.Boolean(default = False)
    created_on = models.DateTimeField(auto_now_add = True)
         
