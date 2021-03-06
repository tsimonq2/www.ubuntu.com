# -*- coding: utf-8 -*-
from django import template
import dateutil.parser

register = template.Library()


@register.filter
def truncate_chars(value, max_length):
    length = len(value)
    if length > max_length:
        truncated = value[:max_length]
        if not length == (max_length + 1) and value[max_length + 1] != " ":
            truncated = truncated[: truncated.rfind(" ")]
        return truncated + "&hellip;"
    return value


@register.filter
def format_date(date):
    date_formatted = dateutil.parser.parse(date)
    return date_formatted.strftime("%-d %B %Y")


@register.filter
def replace_admin(url):
    return url.replace("admin.insights.ubuntu.com", "blog.ubuntu.com")


@register.filter
def keyvalue(dictionary, key_name):
    """
    A template filter to get a dictionary key using a variable.
    E.g.:

    {{ dictionary | keyvalue:variable }}

    (From https://stackoverflow.com/a/10700142/613540)
    """

    return dictionary.get(key_name)
