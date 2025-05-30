from django.contrib.auth import get_user_model
user_model= get_user_model()
from blog.models import Post

from django import template
from django.utils.html import escape, mark_safe, format_html
import logging
logger = logging.getLogger(__name__)


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


@register.simple_tag
def row(extra_classes=''):
    return format_html(f'<div class="row {extra_classes}">')


@register.simple_tag
def endrow():
    return format_html("</div>")


@register.simple_tag
def col(extra_classes=''):
    return format_html(f'<div class="col {extra_classes}">')


@register.simple_tag
def endcol():
    return format_html("</div>")


@register.simple_tag(takes_context=True)
def author_details_tag(context):
    request = context["request"]
    current_user = request.user
    post = context["post"]
    author = post.author

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        prefix = format_html('<a href="mailto:{}">', author.email)
        suffix = format_html("</a>")
    else:
        prefix = ""
        suffix = ""

    return format_html("{}{}{}", prefix, name, suffix)


@register.inclusion_tag("blog/post-list.html")
def recent_posts(post):
    posts = Post.objects.exclude(pk=post.pk)[:5]
    logger.debug("Loaded %d recent posts for post %d", len(posts), post.pk)
    return {"title": "Recent Posts", "posts": posts}


