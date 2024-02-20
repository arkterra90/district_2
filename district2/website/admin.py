from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ContactForm)
admin.site.register(blogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
