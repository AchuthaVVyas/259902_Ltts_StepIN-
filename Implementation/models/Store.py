from random import randint as rnd
from models.Item import Item


class Store:

    def __init__(self):
        self.storeItems = []
        self.item = {'HDMI Cable': 19, 'Ram': 12, 'Mouse': 20, 'Keyboard': 90}
        self.read()

    def read(self):
        for i, j in self.item.items():
            self.storeItems.append(Item(i, float(j)))

    def getStoreItems(self):
        return self.storeItems

    def listStore(self):
        counter = 0
        print("Store Items : ")
        for item in self.storeItems:
            print("%s : %s  $%s" % (counter, item.name, item.price))
            counter += 1
        print("")
