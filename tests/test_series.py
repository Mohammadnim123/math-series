from math_series import __version__
from math_series.series import fibonacci,lucas,sum_series


def test_version():
    assert __version__ == '0.1.0'
    
# -----------------------------------------------------

def test_0():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual

def test_1():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual
    
def test_2():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual

def test_3():
    expected = 2
    actual = fibonacci(3)
    assert expected == actual

def test_4():
    expected = 3
    actual = fibonacci(4)
    assert expected == actual

def test_5():
    expected = 5
    actual = fibonacci(5)
    assert expected == actual    


# ------------------------------------------------------------

def test_6():
    expected = 2
    actual = lucas(0)
    assert expected == actual

def test_7():
    expected = 1
    actual = lucas(1)
    assert expected == actual
    
def test_8():
    expected = 3
    actual = lucas(2)
    assert expected == actual

def test_9():
    expected = 4
    actual = lucas(3)
    assert expected == actual

def test_10():
    expected = 7
    actual = lucas(4)
    assert expected == actual

def test_11():
    expected = 11
    actual = lucas(5)
    assert expected == actual    

# ------------------------------------------------------------

def test_12():
    expected = 0
    actual = sum_series(0)
    assert expected == actual

def test_13():
    expected = 1
    actual = sum_series(1)
    assert expected == actual
    
def test_14():
    expected = 1
    actual = sum_series(2)
    assert expected == actual

def test_15():
    expected = 10
    actual = sum_series(3,4,3)
    assert expected == actual

def test_16():
    expected = 34
    actual = sum_series(4,5,8)
    assert expected == actual

def test_17():
    expected = 6
    actual = sum_series(0,6,2)
    assert expected == actual    