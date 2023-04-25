from lib.gratitude import *

def test_format_gratitude():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "
    
def test_add_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("food")
    assert gratitudes.format() == "Be grateful for: food"

def test_format():
    gratitudes = Gratitudes()
    gratitudes.add("food")
    gratitudes.add("drink")
    gratitudes.add("Pepsi")
    assert gratitudes.format() == "Be grateful for: food, drink, Pepsi"