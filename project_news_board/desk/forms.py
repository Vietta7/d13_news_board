from django import forms
from .models import Reply, Post
from django.contrib.auth.forms import AuthenticationForm
from django import forms



class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), label='Содержимое')

#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'category']


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок поста'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст поста'
            }),

            'image': forms.FileInput
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': "inputPassword"}))