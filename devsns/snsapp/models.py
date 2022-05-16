from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

#게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_body


class freePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class freeComment(models.Model):
    comment_body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(freePost, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_body