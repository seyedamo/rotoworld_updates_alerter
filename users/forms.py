from django import forms
from users.models import User


class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email_address']
