from django.contrib import admin
from .models import Post
from .models import Record

admin.site.register(Post)
admin.site.register(Record)