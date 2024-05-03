from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Stats, PostNews, Media, Contact, Page, Program
from tinymce.widgets import TinyMCE

class ProgamForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['title', 'penanggung_jawab', 'images', 'content'] 

class ProgamForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Program
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'message']

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'images', 'content']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'images', 'content', 'url_drive']

class PostNewsForm(forms.ModelForm):
    class Meta:
        model = PostNews
        fields = ['title', 'images', 'content', 'category'] 

class PostNewsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = PostNews
        fields = '__all__'

class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['students', 'teachers', 'staffs', 'registrations']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', 'is_admin', 'is_staff', 'is_siswa')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data["phone_number"]
        if commit:
            user.save()
        return user
    
