from django.contrib import admin
from .models import Post, Comment, freePost, freeComment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(freePost)
admin.site.register(freeComment)