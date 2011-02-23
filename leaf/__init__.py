#!/usr/bin/env python
# encoding: utf-8

import lxml.html
import unicodedata
import string
from lxml.cssselect import CSSSelector


class Parser:
    """ Simple wrapper around lxml object """
    def __init__(self, element):
        self.element = element
        self.encoding = "utf8"

    def __call__(self, selector):
        """ Simple access to CSSSelector through obj(selector) """
        result = CSSSelector(selector)(self.element)
        return [Parser(element) for element in result]
    css = __call__

    def get(self, selector):
        """ Get first element from CSSSelector """
        elements = self(selector)
        if elements:
            return elements[0]
        return None

    def html(self, encoding="utf8"):
        """ Return html of element """
        return lxml.html.tostring(self.element, encoding=self.encoding)

    def __unicode__(self):
        return lxml.html.tostring(self.element, method='text', encoding=self.encoding).decode(self.encoding)

    def parse(self, func, *args, **kwargs):
        """ Parse element with given function"""
        result = []
        for element in self.xpath('child::node()'):
            if isinstance(element, Parser):
                childrens = element.parse(func, *args, **kwargs)
                element_result = func(element, childrens, *args, **kwargs)
                if element_result:
                    result.append(element_result)
            else:
                result.append(element)
        return u"".join(result)

    def _wrap_result(self, func):
        """ Wrap result in Parser instance """
        def wrapper(*args):
            result = func(*args)
            if hasattr(result, '__iter__'):
                return [self._wrap_element(element) for element in result]
            else:
                return self._wrap_element(result)
        return wrapper

    def _wrap_element(self, result):
        """ Wrap single element in Parser instance """
        if isinstance(result, lxml.html.HtmlElement):
            return Parser(result)
        else:
            return result

    def __getattr__(self, name):
        """  Nice attribution getter modification """
        # Try to get element.attrib
        if name in self.element.attrib:
            return self.element.attrib[name]
        # If attrib with that name doesn't exists return lxml attrib
        result = getattr(self.element, name, None)
        # If result is callable -- decorate it.
        if callable(result):
            return self._wrap_result(result)
        else:
            return result


def parse(html_string):
    """ Parse html with wrapper """
    return Parser(lxml.html.fromstring(html_string))


def str2int(string_with_int):
    """ Collect digits from a string """
    return int("".join([char for char in string_with_int if char in string.digits]) or 0)


def to_unicode(obj, encoding='utf-8'):
    """ Convert string to unicode string """
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj


def strip_accents(s, pass_symbols=[u'й', u'Й', u'\n']):
    """ Strip accents from a string """
    result = []
    for char in s:
        # Pass these symbols without processing
        if char in pass_symbols:
            result.append(char)
            continue
        for c in unicodedata.normalize('NFD', char):
            if unicodedata.category(c) == 'Mn':
                continue
            result.append(c)
    return ''.join(result)


def strip_symbols(s, pass_symbols=[u'й', u'Й', u'\n']):
    """ Strip ugly unicode symbols from a string """
    result = []
    for char in s:
        # Pass these symbols without processing
        if char in pass_symbols:
            result.append(char)
            continue
        for c in unicodedata.normalize('NFKC', char):
            if unicodedata.category(c) == 'Zs':
                result.append(u' ')
                continue
            if unicodedata.category(c) not in ['So', 'Mn', 'Lo', 'Cn', 'Co', 'Cf', 'Cc']:
                result.append(c)
    return u"".join(result)


def strip_spaces(s):
    """ Strip excess spaces from a string """
    return u" ".join([c for c in s.split(u' ') if c])


def strip_linebreaks(s):
    """ Strip excess line breaks from a string """
    return u"\n".join([c for c in s.split(u'\n') if c])
