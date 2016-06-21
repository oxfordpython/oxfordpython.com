from django.conf import settings

import meetup.api


def meetup_group(request):
    mclient = meetup.api.Client(settings.MEETUP_API_KEY)
    return {'meetup': mclient.GetGroup({'urlname': 'oxfordpython'})}
