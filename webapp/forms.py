from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
GENDER = (('M','MALE'),('F','FEMALE'))
User = get_user_model()
class UserForm(forms.ModelForm):
    first_name = forms.CharField(initial='Teja')
    email = forms.CharField(initial='teja@abc.com')
#     email = forms.EmailField(max_length=64, help_text='Enter a valid email address')
    class Meta:
        model = User
        fields = ('first_name','email')
class ProfileForm(forms.ModelForm):
    phone = forms.CharField(initial='+919876543210')
    age = forms.IntegerField(initial=27)
    gender = forms.ChoiceField(choices=GENDER)
    
    address = forms.CharField(initial='wanaparthy')
    class Meta:
        model = Profile
        fields = ('phone','age','gender','address','avatar')

class EducationForm(forms.ModelForm):
    course = forms.CharField(initial='B.Tech')
    college = forms.CharField(initial='KTMCE')
    # year = forms.IntegerField(initial=2002)
    percentage = forms.FloatField(initial=69.38)
    class Meta:
        model = Education
        exclude = ('user', )
        # fields = ('course','college','year','percentage')
