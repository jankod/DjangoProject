from django import template
from django.http import request
from django.template import context, RequestContext
from django.urls.resolvers import get_resolver, URLResolver
from django.urls import reverse, NoReverseMatch
from django.utils.encoding import escape_uri_path

register = template.Library()


@register.simple_tag(takes_context=True)
def template_name(context: RequestContext):
    # TODO: check if dev mode
    req: request = context['request']
    path: URLResolver = get_resolver(req.path)
    return 'nesto radi, zbogno: ' + context.template_name


@register.simple_tag(takes_context=True)
def active_link(context, view_name):
    r = reverse(view_name)
    req: request = context['request']
    path = reverse(view_name)

    request_path = escape_uri_path(req.path)

    if request_path == path:
        return 'active'

    return ''
