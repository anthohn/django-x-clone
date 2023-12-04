from django import template
from django.utils import timezone

MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def get_posted_at_display(posted_at):
    seconds_ago = (timezone.now() - posted_at).total_seconds()
    if seconds_ago <= MINUTE:
        return f'Maintenant'
    elif seconds_ago <= HOUR:
        return f'{int(seconds_ago // MINUTE)}min'
    elif seconds_ago <= DAY:
        return f'{int(seconds_ago // HOUR)}h'


@register.simple_tag(takes_context=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'vous'
    return user.username