from django import forms
from users.models import User


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email_address']
