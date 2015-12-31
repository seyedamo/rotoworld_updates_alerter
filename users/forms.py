from django import forms
from users.models import User


class SignUpForm(forms.ModelForm):
    model = User
    email_address = forms.EmailField(label="email_address")