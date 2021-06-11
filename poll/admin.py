from django.contrib import admin
from .models import Polls, Choice
# Register your models here.
admin.site.register(Polls)
admin.site.register(Choice)