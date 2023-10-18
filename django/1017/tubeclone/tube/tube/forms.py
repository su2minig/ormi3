from django import forms
from .models import Post


class CommentForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'