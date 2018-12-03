from django.contrib import admin

# Register your models here.
from movies.models import Review, Comment

admin.site.register(Review)
admin.site.register(Comment)
