# -*- coding: utf-8 -*-

from productquality import recalculate_quality, Product

    
def test_Bintje():
    Bintje = Product("potato",8)
    recalculate_quality(Bintje)
    assert Bintje.quality == 7.5
    
def test_Brie():
    Brie = Product("cheese",5)
    recalculate_quality(Brie)
    assert Brie.quality == 3

def test_Tomato():
    Tomato = Product("Tomato",9)
    recalculate_quality(Tomato)
    assert Tomato.quality == 9
    
def test_olives():
    olives = Product("olives",4)
    recalculate_quality(olives)
    assert olives.quality == 1