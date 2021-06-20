from django.shortcuts import render
from .models import Topic, Question, UserAvatar
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method =='GET':
        topics=Topic.objects.all()
    return render(request,'index.html',{
        'topics':topics,
        })
def quesbytopic(request,id):
    if request.method=='GET':
        questions=Question.objects.filter(topic=id)
        profile=UserAvatar.objects.filter(user=request.user.pk)
        return render(request,'questions.html',{
            'questions':questions,
            'profile':profile,
        })
def questionview(request,id):
    Qviews=Question.objects.get(id=id)
    print(Qviews.views)
    Qviews.views=Qviews.views+1
    Qviews.save()
    return render(request,'single-topic.html',{
        'question':Qviews,
    })
    