from django.contrib import admin
from .models import Topic, Question, UserAvatar, Answers
# Register your models here.
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(UserAvatar)
admin.site.register(Answers)