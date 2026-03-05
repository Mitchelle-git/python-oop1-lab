import pytest
from lib.coffee import Coffee

def test_coffee_creation():
    c = Coffee("Latte", "Medium", 3.5, 120)
    assert c.coffee_type == "Latte"
    assert c.size == "Medium"
    assert c.price == 3.5
    assert c.caffeine_content == 120
    assert not c.is_brewed

def test_brew():
    c = Coffee("Latte", "Medium", 3.5, 120)
    result = c.brew()
    assert c.is_brewed
    assert "Brewing" in result

def test_drink():
    c = Coffee("Latte", "Medium", 3.5, 120)
    msg = c.drink(50)
    assert c.caffeine_content == 70
    assert "Caffeine remaining" in msg

def test_get_info():
    c = Coffee("Latte", "Medium", 3.5, 120)
    info = c.get_info()
    assert "Latte" in info
    assert "120mg" in info