from django import forms
from django.forms.widgets import CheckboxInput

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    private = forms.BooleanField(required = False)

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'private' : CheckboxInput(attrs = {'class': 'checkbox'}),   
        }


class EntryForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs = {'cols': 80})}