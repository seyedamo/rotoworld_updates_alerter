from __future__ import unicode_literals

from django.db.models import Model, EmailField


class User(Model):
    email_address = EmailField(unique=True)

    def get_absolute_url(self):
        return "http://rotoworld-updates.herokuapp.com/signup/"
