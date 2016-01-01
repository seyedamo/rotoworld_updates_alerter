from __future__ import unicode_literals

from django.db.models import Model, EmailField


class User(Model):
    email_address = EmailField()

    def get_absolute_url(self):
        pass