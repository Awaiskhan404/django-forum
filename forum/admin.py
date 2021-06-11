from django.contrib import admin
from .models import Forum, Topic, Question
# Register your models here.
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Question)