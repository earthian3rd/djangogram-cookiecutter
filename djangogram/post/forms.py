from pyexpat import model
from django import forms
from . models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image'] 
        label = {
            'caption' : '내용',
            'image' : '사진'
        }