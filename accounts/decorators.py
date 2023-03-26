from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse
from venues.models import Venue, Section, Table


def has_section_table(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        venue = Venue.objects.get(user=request.user)
        sections = Section.objects.filter(venue=venue)
        if sections.exists():
            for section in sections:
                tables = Table.objects.filter(section=section)
                if tables.exists():
                    return f(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('accounts:create_section_table'))

    return wrapper
