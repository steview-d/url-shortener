from django.shortcuts import render

from .forms import PrivateUrlObjectForm, UrlObjectForm

import random
import string


def index(request):
    """Main page"""

    user_active = True if request.user.is_authenticated else False

    # Initialise specific form depending if a user is logged in
    url_form = PrivateUrlObjectForm if user_active else UrlObjectForm

    if 'shorten-url-form' in request.POST:

        form = PrivateUrlObjectForm(request.POST) if user_active \
            else UrlObjectForm(request.POST)

        if form.is_valid():

            form = form.save(commit=False)

            # create short_path value
            chars = string.ascii_lowercase + string.digits
            form.short_path = ''.join((random.choice(chars) for i in range(5)))

            # if form contains tag values, add these to the tags ArrayField
            tag_list = []
            for tag in ['tag_one', 'tag_two', 'tag_three']:
                if request.POST.get(tag):
                    tag_list.append(request.POST[tag])
            form.tags = tag_list

            form.save()

        else:
            url_form = form

    context = {'url_form': url_form, }

    return render(request, "index.html", context)
