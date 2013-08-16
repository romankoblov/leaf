#!/usr/bin/env python
# encoding: utf-8
import sys
from os.path import abspath, dirname

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import leaf


sample = open('tests/sample.html').read()

def test_selectors():
    document = leaf.parse(sample)
    links = document('div#menu a')
    assert links[-1].text == 'Contacts', "Access by id and element type"
    links2 = document('div#menu li a')
    assert links2[-1].text == ' Test link 5', "Access by id and element type 2"
    assert len(document('a')) == 9
    assert document('li.active_link a')[0].text == ' Test link 5', "Access by class"

def test_attribs():
    document = leaf.parse(sample)
    first_link = document.get('div#menu li')
    assert document.get('div#menu a', 4).text == ' Test link 5', "Get element by index"
    assert document.get('div#menu a', 99, default='blah') == 'blah', "Custom default value for get"
    assert bool(document.get('div#menu li')) == True, "Node bool"
    assert bool(document.get('div#menu_test li')) == False, "Node bool"
    assert isinstance(first_link, leaf.Parser), "Get first element"
    assert first_link.id == 'first_link', "Id attrib"
    assert first_link.onclick == "alert('test')", "Onclick attrib"
    first_link.onclick = 'blah()'
    assert first_link.onclick == 'blah()', "Attribute modification"

def test_html():
    document = leaf.parse(sample)
    link = document.get('div#content li.link2')
    assert link.html() == '<li class="link2"><a href="#3"> Test link3</a></li>\n\t\t', "Convert element to html code"

def test_inner_methods():
    document = leaf.parse(sample)
    link = document.xpath('body/div/ul/li[@class="active_link"]')[0]
    assert link.get('a').text == ' Test link 5', 'XPath by inner lxml method'

def test_inner_html():
    html = '''<div>xxx <!-- comment --> yyy <p>foo</p> zzz</div>'''
    dom = leaf.parse(html)
    assert dom.inner_html() == 'xxx <p>foo</p> zzz'

if __name__ == '__main__':
    test_selectors()
    test_attribs()
    test_html()
    test_inner_methods()
    test_inner_html()
