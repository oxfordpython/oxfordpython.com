from django.conf import settings
from django.core.cache import cache

import meetup.api

MEETUP_CACHE_KEY = 'meetup_getgroup'


def meetup_group(request):
    group = cache.get(MEETUP_CACHE_KEY)
    if not group:
        mclient = meetup.api.Client(settings.MEETUP_API_KEY)
        group = mclient.GetGroup({'urlname': 'oxfordpython'})
        cache.set(MEETUP_CACHE_KEY, group, 600) # Cache for 10mins, because caching
    return {'meetup': group}
