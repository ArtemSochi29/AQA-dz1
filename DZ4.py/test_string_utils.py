import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

@pytest.mark.parametrize('str, result', [ ("artem", "Artem")  ])

def test_capitilize(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    assert res == result

@pytest.mark.parametrize('str, result', [ ("    Artem", "Artem")  ])

def test_trim(str, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    assert res == result

@pytest.mark.parametrize('str, delimeter, result' , [ ("a,b,c,d", "," , ['a', 'b', 'c', 'd']), ("1:2:3:4", ":", ['1', '2', '3','4'])  ])

def test_to_list(str, delimeter, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(str, delimeter)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [ ("Asrtem", "s", "Artem"), ("OkArtem", "Ok", "Artem") ])

def test_delete(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, str1)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [("Artem", "A", True), ("Artem", "t", False)])

def test_starts_with(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(str, str1)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [("Artem", "m", True), ("Artem", "t", False)])

def test_end_with(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(str, str1)
    assert res == result

@pytest.mark.parametrize('str, result', [("", True), ("   ", True), ("Artem", False)])

def test_is_empty(str, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(str)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [("1,2,3,4", ",", ["1,2,3,4"] ), ("Artem, Bas", ",","[Artem, Bas]"), ("Bas", "-", "B-a-s" )])

def test_list_to_string(lst, joiner, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res == result