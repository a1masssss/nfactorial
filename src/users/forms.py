from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Name (optional)',
            'class': 'form-control',
            'autocomplete': 'off'
        })

        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Surname (optional)',
            'class': 'form-control',
            'autocomplete': 'off'
        })

        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
            'class': 'form-control',
            'autocomplete': 'off'
        })
        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })
        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm your password',
            'class': 'form-control',
            'autocomplete': 'new-password'
        })


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''

        self.fields['username'].widget.attrs.update({
            'placeholder':'Email', 
            'class':'form-control',
            'autocomplete': 'new-password'
        })

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Password', 
            'class': 'form-control', 
            'autocomplete': 'new-password'
        })

        for field in self.fields.values():
            field.lavel =  ''

    username = forms.EmailField(label='Email')