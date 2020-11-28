from django.shortcuts import render

from .forms import UrlObjectForm


def index(request):
    """Front page"""

    url_form = UrlObjectForm()

    context = {'url_form': url_form, }

    return render(request, "index.html", context)
