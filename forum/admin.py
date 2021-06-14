from django.contrib import admin
from .models import Forum, Topic, Question, Category
# Register your models here.
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Question)
admin.site.register(Category)