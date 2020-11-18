"""
Miscellaneous helper functions
"""

import re

from bs4 import BeautifulSoup
from bs4.element import Tag


def find_all(soup, name=None, attrs=None, recursive=True, text=None,
              limit=None, **kwargs):
    """The `find` and `find_all` methods of `BeautifulSoup` don't handle the
    `text` parameter combined with other parameters. This is necessary for
    e.g. finding links containing a string or pattern. This method first
    searches by text content, and then by the standard BeautifulSoup arguments.

    """
    if text is None:
        return soup.find_all(
            name, attrs or {}, recursive, text, limit, **kwargs
        )
    tags = soup.find_all(
        name, attrs or {}, recursive, **kwargs
    )
    rv = []

    def _match_text(tag):
        if isinstance(text, str):
            return text in tag
        return text.search(tag)

    for tag in tags:
        if _match_text(str(tag)):
            rv.append(tag)
        if limit is not None and len(rv) >= limit:
            break
    return rv


def find(soup, name=None, attrs=None, recursive=True, text=None, **kwargs):
    """Modified find method; see `find_all`, above.

    """
    tags = find_all(
        soup, name, attrs or {}, recursive, text, 1, **kwargs
    )
    if tags:
        return tags[0]


def ensure_soup(value, parser=None):
    """Coerce a value (or list of values) to Tag (or list of Tag).

    :param value: String, BeautifulSoup, Tag, or list of the above
    :param str parser: Parser to use; defaults to BeautifulSoup default
    :return: Tag or list of Tags

    """
    if isinstance(value, BeautifulSoup):
        return value.find()
    if isinstance(value, Tag):
        return value
    if isinstance(value, list):
        return [
            ensure_soup(item, parser=parser)
            for item in value
        ]
    parsed = BeautifulSoup(value, features=parser)
    return parsed.find()


def lowercase_attr_names(tag):
    """Lower-case all attribute names of the provided BeautifulSoup tag.
    Note: this mutates the tag's attribute names and does not return a new
    tag.

    :param Tag: BeautifulSoup tag

    """
    tag.attrs = {key.lower(): value for key, value in tag.attrs.items()}
