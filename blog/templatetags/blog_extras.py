from django.contrib.auth import get_user_model
user_model= get_user_model()

from django import template
from django.utils.html import escape, mark_safe, format_html

register = template.Library()

@register.filter
def author_details(author, current_user):
    if not isinstance(author, user_model):
        return ''

    if author == current_user:
        return format_html('<strong>me</strong>')

    if author.first_name and author.last_name:
        name = f'{author.first_name} {author.last_name}'
    else:
        name = author.username

    if author.email:
        email = author.email
        prefix = format_html(f'<a href="mailto:{email}">')
        suffix = format_html('</a>')
    else:
        prefix = ''
        suffix = ''

    print(f'{prefix}{name}{suffix}')
    return format_html(f'{prefix}{name}{suffix}')

    return name