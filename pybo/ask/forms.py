from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        
        # bootstrap 적용
        widgets = {
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control','rows':10}),
        }
        
        labels = {
            'subject': '제목',
            'content': '내용',
        }