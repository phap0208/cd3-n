from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Course, Lesson



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'instructor', 'description']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['course', 'title', 'content']
class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
class YourForm(forms.Form):
    your_field = forms.CharField(
        label="Your Field",
        required=True,
        error_messages={
            'required': "Custom error message for the required field.",
        }
    )

