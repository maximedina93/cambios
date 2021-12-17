from django.contrib import admin

from apps import post

from .models import categoria, post


admin.site.register(categoria)
admin.site.register(post)