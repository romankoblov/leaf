# Leaf


[![image](https://travis-ci.org/romankoblov/leaf.png?branch=master)](https://travis-ci.org/romankoblov/leaf)
[![Coverage Status](https://coveralls.io/repos/github/romankoblov/leaf/badge.svg?branch=master)](https://coveralls.io/github/romankoblov/leaf?branch=master)
[![Downloads](https://img.shields.io/pypi/dm/Leaf.svg)](https://pypi.python.org/pypi/Leaf/)
[![Latest Version](https://img.shields.io/pypi/v/leaf.svg)](https://pypi.python.org/pypi/leaf/)
[![License](https://img.shields.io/pypi/l/Leaf.svg)](https://pypi.python.org/pypi/Leaf/)

What is this?
=============

This is a simple wrapper around [lxml](http://lxml.de/) which adds some
nice features to make working with lxml better. This library covers all
my needs in HTML parsing.

Dependencies
============

[lxml](http://lxml.de/) obviously :3

Features
========

-   Nice jquery-like CSS selectors
-   Simple access to element attributes
-   Easy way to convert HTML to other formats (bbcode, markdown, etc.)
-   A few nice functions for working with text
-   And, of course, all original features of lxml

Description
===========

The main function of the module (for my purposes) is `leaf.parse`. This
function takes an HTML string as argument, and returns a `leaf.Parser`
object, which wraps an lxml object.

With this object you can do anything you want, for example:

    document = leaf.parse(sample)
    # get the links from the DIV with id 'menu' using CSS selectors
    links = document('div#menu a')

Or you can do this:

    # get first link or return None
    link = document.get('div#menu a')

And you can get attributes from these results like this:

    print link.onclick

You can also use standard lxml methods like `object.xpath`, and they
return results as `leaf.Parser` objects.

My favorite feature is parsing HTML into bbcode (markdown, etc.):

    # Let's define simple formatter, which passes text
    # and wraps links into [url][/url] (like bbcode)
    def code_formatter(element, children):
        # Replace <br> tag with line break
        if element.tag == 'br':
            return '\n'
        # Wrap links into [url][/url]
        if element.tag == 'a':
            return u"[url=link}]{text}[/url]".format(link=element.href, text=children)
        # Return children only for other elements.
        if children:
            return children

This function will be recursively called with element and children (this
is string with children parsing result).

So, let\'s call this parser on some `leaf.Parser` object:

```py
document.parse(code_formatter)
```

More detailed examples available in the tests.

Finally, this library has some nice functions for working with text:

| Name             | Description                              |
| ---------------- | ---------------------------------------- |
| to_unicode       | Convert string to unicode string         |
| strip_accents    | Strip accents from a string              |
| strip_symbols    | Strip ugly unicode symbols from a string |
| strip_spaces     | Strip excess spaces from a string        |
| strip_linebreaks | Strip excess line breaks from a string   |
