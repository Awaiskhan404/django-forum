
from django.urls import path
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('questions/<int:id>',views.quesbytopic,name="question"),
    path('question/<int:id>',views.questionview,name="questionview"),
    path('questions/new',views.addquestion,name="addquestion")
]