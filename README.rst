Leaf
====
What is this?
-------------
This is a simple wrapper around lxml, which adds some nice features,
which make work with lxml better. This library covers all my needs in
html parsing.

Dependencies
------------
`lxml <http://lxml.de/>`_ obviously :3

Features
--------
 * Nice jquery-like css selectors
 * Simple access to element attributes
 * Easy way for convert html to other format (bbcode, markdown, etc)
 * Few nice functions for work with text
 * And, of course this saves all original features of lxml

Description
-----------
Main function of module (as I mind) is leaf.parse, this function takes string with 
html as an argument, and returns leaf.Parser object, which wraps lxml object.
With this object you can do anything you want, like this::

	document = leaf.parse(sample)
	links = document('div#menu a') # get links in div with id menu through css selectors

Or you can do this::

	link = document.get('div#menu a') # get first link or return None

And you can get attributes from these results like this::

	print link.onclick

Anyway, you can use standard lxml methods like object.xpath, and they returns results 
wrapped into leaf.Parser.
So, my favorite feature is parsing html into bbcode (markdown, etc)::

	# Lets define simple formatter, which pass text 
	# and wraps links into [url][/url] (like bbcode)
	def omgcode_formatter(element, childrens):
		# Replace <br> tag with line break
	    if element.tag == 'br':
	        return '\n'
		# Wrap links into [url][/url]
	    if element.tag == 'a':
	        return u"[url=link}]{text}[/url]".format(link=element.href, text=childrens)
		# Return childrens only for other elements.
	    if childrens:
	        return childrens

This function will be recursively called with element and childrens (this is string with 
childrens parsing result).
So, lets call this parser in some leaf.Parser object::

	document.parse(omgcode_formatter)

More detailed examples availible in the tests.

Finally, this library has some nice functions for work with text:

*to_unicode* -- Convert string to unicode string

*strip_accents* -- Strip accents from a string

*strip_symbols* -- Strip ugly unicode symbols from a string

*strip_spaces* -- Strip excess spaces from a string

*strip_linebreaks* -- Strip excess line breaks from a string