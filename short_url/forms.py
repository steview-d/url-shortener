from django import forms

from .models import UrlObject


class UrlObjectForm(forms.ModelForm):
    """Form for providing a url to be shortened"""

    class Meta:
        model = UrlObject
        fields = ['long_url']

    def __init__(self, *args, **kwargs):
        super(UrlObjectForm, self).__init__(*args, **kwargs)
        self.fields['long_url'].label = "Url to be shortened:"
