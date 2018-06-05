from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article
from django.forms import ModelForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
		
class AddArticleForm(ModelForm):
    """docstring for ClassName"""
    class Meta:
        model = Article
        fields = ['article_name','article_post','owner']
        widgets={
                    
                    "article_name": forms.Textarea(attrs={'cols': 80, 'rows': 1}),
                    "article_post": forms.Textarea(attrs={'cols': 80, 'rows': 10}),
                 }
    def __init__(self, *arg, **kwargs):
        kwargs.setdefault('label_suffix', '') 
        super(AddArticleForm, self).__init__(*arg, **kwargs)
        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['article_name'].required = True
        self.fields['article_post'].required = True
        self.fields['article_name'].label = 'Article Name'
        self.fields['article_post'].label = 'Your Post'

        


