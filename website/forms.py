from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}))
  first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), required=True)
  last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), required=True)

  class Meta:
    model = User
    fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

  def __init__(self, *args, **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username', 'label': '', 'help_text': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'})

    self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password', 'label': '', 'help_text': 'Your password can’t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can’t be a commonly used password. Your password can’t be entirely numeric.'})
    self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password', 'label': '', 'help_text': 'Enter the same password as before, for verification.'})


class RecordModelForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'pin_code']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pin Code'}),
        }
   