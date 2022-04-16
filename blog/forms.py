from .models import Comment
from .models import Blog
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"