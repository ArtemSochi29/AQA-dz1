import pytest
from stringUtils import StringUtils

stringUtils = StringUtils()

@pytest.mark.parametrize('str, result',  [ 
        ("artem", "Artem"),
        pytest.param("artem", "artem", marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("Artem", "artem", marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("", "", marks=pytest.mark.xfail(reason="Негативная проверка"))  
        ])

def test_pos_capitilize(str, result):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(str)
    assert res == result

@pytest.mark.parametrize('str, result', [
        ("    Artem", "Artem"),
        pytest.param("artem", "", marks=pytest.mark.xfail(reason="Негативная проверка")), 
        pytest.param("", "", marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("", "artem", marks=pytest.mark.xfail(reason="Негативная проверка"))
        ])

def test_pos_trim(str, result):
    stringUtils = StringUtils()
    res = stringUtils.trim(str)
    assert res == result

@pytest.mark.parametrize('str, delimeter, result' , [ 
        ("a,b,c,d", "," , ['a', 'b', 'c', 'd']), 
        ("1:2:3:4", ":", ['1', '2', '3','4']),
        pytest.param("a,b", ",", [], marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("", "", [], marks=pytest.mark.xfail(reason="Негативная проверка"))  
        ])

def test_pos_to_list(str, delimeter, result):
    stringUtils = StringUtils()
    res = stringUtils.to_list(str, delimeter)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [
        ("Asrtem", "s", "Artem"), 
        ("OkArtem", "Ok", "Artem"),
        pytest.param("", "", "", marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("   artem", "ar", "tem", marks=pytest.mark.xfail(reason="Негативная проверка")) 
        ])

def test_pos_delete(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(str, str1)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [
        ("Artem", "A", True), 
        ("Artem", "t", False),
        pytest.param("", "", True, marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("", "", False, marks=pytest.mark.xfail(reason="Негативная проверка"))
        ])

def test_pos_starts_with(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(str, str1)
    assert res == result

@pytest.mark.parametrize('str, str1, result', [
        ("Artem", "m", True), 
        ("Artem", "t", False),
        pytest.param("", "", True, marks=pytest.mark.xfail(reason="Негативная проверка")),
        pytest.param("", "", False, marks=pytest.mark.xfail(reason="Негативная проверка"))
        ])

def test_pos_end_with(str, str1, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(str, str1)
    assert res == result

@pytest.mark.parametrize('str, result', [
        ("", True), 
        ("   ", True), 
        ("Artem", False),
        pytest.param("__", True, marks=pytest.mark.xfail(reason="Негативная проверка"))
        ])

def test_pos_is_empty(str, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(str)
    assert res == result

@pytest.mark.parametrize('lst, joiner, result', [
        ("1,2,3,4", ",", ["1,2,3,4"] ), 
        ("Artem, Bas", ",","[Artem, Bas]"), 
        ("Bas, Artem", "-", "Bas-Artem" )
        ])
@pytest.mark.xfail()
def test_pos_list_to_string(lst, joiner, result):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res == result