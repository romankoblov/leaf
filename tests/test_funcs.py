#!/usr/bin/env python
# encoding: utf-8
import sys
sys.path.append("../leaf")
import leaf
from six import text_type


def test_str2int():
    assert leaf.str2int('blah333$$233da3') == 3332333, "Collect digits from a string"


def test_to_unicode():
    assert isinstance(leaf.to_unicode("test"), text_type)
    assert isinstance(leaf.to_unicode(u"blah"), text_type)
    assert isinstance(leaf.to_unicode(b"blah"), text_type)


def test_strip_accents():
    assert leaf.strip_accents(u'ЁёЇїIiӒӓЎўй') == u'ЕеІіIiАаУуй', "Strip accents from a string"


def test_strip_symbols():
    bad_string = u"""b̼̘̬ͭ͂̈́̀l͇͉̱͚̲̗̗͞a̱̭̬͎͉̤ͨ͂̌̑̓͂͐h̬̯̻̩͗ͩͯb̢̬͕͈̥̅̌͆̔̉ͅĺ̘̖̼͚͒̈́̏͌̃͟ ͎̮̫̍ͫ̽͐͋ͤ͂a̜͔̩͇̩̪͐̍̐̃ͤ͑ ̦̌ḧ̙̝͓̜͕̝́ͅb̛̞͔̽̃̍ͪla̘̠͖͍̣͙̝͌ͪ͒̃ͯ ͗͛̆͊.̛̭̜̞̲͓̯ͧ̅h͂͑/̢̊/̠̘͖͖̖̺̯"""
    assert leaf.strip_symbols(bad_string) == u'blahbl a hbla .h//'


def test_strip_spaces():
    assert leaf.strip_spaces(
        '   blah    sdsdf a         adddd d         ') == 'blah sdsdf a adddd d', "Strip excess spaces from a string"


def test_strip_linebreaks():
    assert leaf.strip_linebreaks("blah\n\n\n\ntest") == 'blah\ntest', "Strip excess line breaks from a string"

if __name__ == '__main__':
    test_str2int()
    test_to_unicode()
    test_strip_accents()
    test_strip_symbols()
    test_strip_spaces()
    test_strip_linebreaks()
