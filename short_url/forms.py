from django import forms

from .models import UrlObject


class UrlObjectForm(forms.ModelForm):
    """Form for providing a url to be shortened"""

    class Meta:
        model = UrlObject
        fields = ['long_url']


class PrivateUrlObjectForm(UrlObjectForm):
    """Extend the UrlObjectForm with tag fields"""

    def __init__(self, *args, **kwargs):
        super(UrlObjectForm, self).__init__(*args, **kwargs)
        self.fields['tag_one'] = forms.CharField()
        self.fields['tag_two'] = forms.CharField()
        self.fields['tag_three'] = forms.CharField()
