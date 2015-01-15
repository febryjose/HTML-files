from django import forms
from models import *

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
       
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserReg
        widgets = {
                   'address':forms.Textarea(attrs = {'cols' : 60, 'rows' : 5}),
                   'profileimage': forms.FileInput()
        }
        fields = [ 'address', 'profileimage']



class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',]





        
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'password']
        
    
        
