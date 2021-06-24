from django.shortcuts import render
from .models import Topic, Question, UserAvatar, Answers
from django.contrib.auth.models import User
from . forms import QuestionForm
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
    Qans=Answers.objects.filter(question=id).order_by('date')
    print(Qans)
    Qviews.views=Qviews.views+1
    Qviews.save()
    return render(request,'single-topic.html',{
        'question':Qviews,
        'replies':Qans,
    })
def addquestion(request):
    form=QuestionForm()
    return render(request,'create-topic.html',{
        'form':form,
    })