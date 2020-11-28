from django.shortcuts import render

from .forms import UrlObjectForm


def index(request):
    """Front page"""

    url_form = UrlObjectForm()

    if 'shorten-url-form' in request.POST:

        form = UrlObjectForm(request.POST)
        print(form)
        form.save()

    context = {'url_form': url_form, }

    return render(request, "index.html", context)
