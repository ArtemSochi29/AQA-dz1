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

