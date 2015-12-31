from django import forms


class SignUpForm(forms.ModelForm):
    email_address = forms.EmailField(label="email_address")