#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append("../leaf")
import leaf
sample = open('tests/sample2.html').read()
sample_result = open('tests/bbcode_result.txt').read()


def bbcode_formatter(element, children, site):
    if element.tag == 'br':
        return '\n'
    if element.tag == 'a':
        return u"[url={site}/redirect.php?url={link}]{text}[/url]".format(site=site, link=element.href, text=children)
    if element.tag == 'img':
        return u"[img={link}]{text}[/img]".format(link=element.src, text=children)
    if element.tag in ['b', 'strong']:
        return u"[b]{text}[/b]".format(text=children)
    if element.tag in ['em', 'i']:
        return u"[i]{text}[/i]".format(text=children)
    if element.tag in ['del', 's']:
        return u"[s]{text}[/s]".format(text=children)
    if element.tag == 'u':
        return u"[u]{text}[/u]".format(text=children)
    if element.tag == 'title':
        return u""
    if children:
        return children


def test_bbcode():
    document = leaf.parse(sample)
    bbcode = document.parse(bbcode_formatter, 'http://example.com/')
    bbcode = leaf.strip_spaces(bbcode)
    bbcode = leaf.strip_symbols(bbcode)
    bbcode = leaf.strip_linebreaks(bbcode)

    assert bbcode == leaf.to_unicode(sample_result), "Sample bbcode formatter"

if __name__ == '__main__':
    test_bbcode()
