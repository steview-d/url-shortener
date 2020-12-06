from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from .forms import UrlObjectForm
from .models import UrlObject

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

            # need to add check to ignore paths in use
            # and already created short_paths

            form.save()
        else:
            url_form = form

    # Create list of public short urls
    public_urls = UrlObject.objects.filter(public=True).order_by('-added')[:10]

    print(public_urls)

    context = {'url_form': url_form,
               'public_urls': public_urls,
               'app_domain': settings.APP_DOMAIN, }

    return render(request, "index.html", context)


def url_redirect(request, short_url):
    """Redirect to actual url"""

    try:
        redirect_to = UrlObject.objects.get(short_path=short_url)
    except ObjectDoesNotExist:
        return redirect('index')

    u = UrlObject.objects.get(
        short_path=short_url
    )
    u.clicks += 1
    u.save()

    return redirect(redirect_to.long_url)
