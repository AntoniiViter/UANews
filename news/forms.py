from django.forms import ModelForm
from .models import News, Comments
from django import forms

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'info', 'image', 'url']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['info']