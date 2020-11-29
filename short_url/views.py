from django.shortcuts import render

from .forms import UrlObjectForm

import random
import string


def index(request):
    """Main page"""

    # Initialise specific form depending if a user is logged in
    url_form = UrlObjectForm

    if 'shorten-url-form' in request.POST:
        form = UrlObjectForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            # create short_path value
            chars = string.ascii_lowercase + string.digits
            form.short_path = ''.join((random.choice(chars) for i in range(5)))

            form.save()
        else:
            url_form = form

    context = {'url_form': url_form, }

    return render(request, "index.html", context)
