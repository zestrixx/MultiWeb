from django.contrib import admin
from .models import shorturl, Issues

# Register your models here.

admin.site.register(shorturl)
admin.site.register(Issues)