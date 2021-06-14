from django.shortcuts import render
from .models import Category, Forum, Topic, Question
# Create your views here.
def index(request):
    if request.method =='GET':
        for topics in Topic.objects.all():
            num_posts=topics.num_posts()
            sum_visits=topics.sum_visits()
    return render(request,'index.html',{
        'topics':topics,
        'num_posts':num_posts,
        'sum_visits':sum_visits,
        })