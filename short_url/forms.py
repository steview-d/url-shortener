from django import forms
from django.contrib.postgres.forms import SimpleArrayField

from .models import UrlObject


class UrlObjectForm(forms.ModelForm):
    """Form for providing a url to be shortened"""

    class Meta:
        model = UrlObject
        fields = ['long_url']
