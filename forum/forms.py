from django import forms
from .models import Question, Topic



class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title','topic','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter Title'}),
            
        }