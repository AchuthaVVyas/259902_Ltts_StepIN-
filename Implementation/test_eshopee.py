from models.ShoppingCart import *
from models.Store import *
from models.Item import *
from eshopee import *
from main import *


def test_getStoreItems():
    store1 = Store()
    assert len(store1.getStoreItems()) == len(Store.getStoreItems(Store()))

def test_getTotalPrice():
    shop = ShoppingCart()
    shop.items = []
    assert sum(shop.items) == ShoppingCart.getTotalPrice(ShoppingCart())

def test_getCartItems():
    cart1 = ShoppingCart()
    assert len(cart1.getCartItems()) == len(ShoppingCart.getCartItems(ShoppingCart()))
