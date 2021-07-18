import tkinter as tk
from tkinter.font import Font
from tkinter import *
from tkinter import messagebox
from models.Store import Store
from models.ShoppingCart import ShoppingCart
import datetime


def viewStore():
    global storeWindow

    storeLabelFrame = LabelFrame(storeWindow, text="Store Items",)
    storeLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    storeItemsFrame = Frame(storeLabelFrame)
    storeItemsFrame.pack(padx="10", pady="5")
    store = Store()
    storeItems = store.getStoreItems()
    for item in storeItems:
        itemFrame = Frame(storeItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,
                          font=("Candara", 15), fg="blue")
        priceLabel = Label(itemFrame, text="Rs.%s" %
                           item.price, font=("Candara", 13), fg="red")
        addToCartBtn = Button(itemFrame, text="Add To Cart",
                              cursor="hand2", command=lambda i=item: addItemToCart(i))
        btnImage = PhotoImage(file="F:\python_project\Eshopping\images\\addTocart.png")
        addToCartBtn.image = btnImage
        addToCartBtn.config( image=btnImage,width="40", height="40")

        nameLabel.pack(side="left")
        priceLabel.pack(side="left", fill="both", expand="yes")
        addToCartBtn.pack(side="right")

    btnGoCart = Button(storeWindow, text="Go To Cart", font=(
        "Candara", 15, "bold"), fg="red", bg="white", cursor="hand2", command=viewCart)
    btnGoCart.pack(pady="6")


def viewCart():
    cartWindow = Toplevel()
    cartWindow.title("The Cart")
    cartWindow.grab_set()
    global cart
    cartItems = cart.getCartItems()

    cartItemsLabelFrame = LabelFrame(cartWindow, text="Cart Items")
    cartItemsLabelFrame.pack(fill="both", expand="yes", padx="20", pady="10")

    cartItemsFrame = Frame(cartItemsLabelFrame, padx=3, pady=3)
    cartItemsFrame.pack()
    index = 0
    for item in cartItems:
        itemFrame = Frame(cartItemsFrame,  pady="5")
        itemFrame.pack(fill="both", expand="yes")

        nameLabel = Label(itemFrame, text=item.name,
                          font=("Candara", 15), fg="blue")
        priceLabel = Label(itemFrame, text=" Rs.%s" %
                           item.price, font=("Candara", 13), fg="red")
        addToCartBtn = Button(itemFrame, text="Remove From Cart", font=("Candara", 11, "bold"),
                              fg="red", bg="white", cursor="hand2", command=lambda i=index: removeFromCart(i, cartWindow))

        nameLabel.pack(side="left")
        priceLabel.pack(side="left")
        addToCartBtn.pack(side="right")
        index += 1

    checkOutFrame = Frame(cartWindow, pady="10")
    totalPriceLabel = Label(checkOutFrame, text="Total Price : Rs.%s" %
                            cart.getTotalPrice(), font=("Candara", 14, "bold"), fg="indigo")
    totalPriceLabel.pack(side="left")
    buyBtn = Button(checkOutFrame, text="Buy Now", font=("Candara", 15, "bold"),
                    fg="indigo", bg="white", cursor="hand2", command=lambda: buyCommand(cartWindow))
    buyBtn.pack(side="left", padx="10")
    checkOutFrame.pack()

    backToStoreBtn = Button(cartWindow, text="Back To Store", font=(
        "Candara", 15, "bold"), fg="red", bg="white", cursor="hand2", command=cartWindow.destroy)
    backToStoreBtn.pack(pady="6")

    cartWindow.mainloop()


def addItemToCart(item=None):
    global cart
    cart.addToCart(item)
    messagebox.showinfo(
        title="Success", message="Item %s Added To The Cart !!" % item.name)


def removeFromCart(itemIndex=None, cartWindow=None):
    global cart
    cart.removeFromCart(itemIndex)
    messagebox.showinfo(title="success", message="Item Removed")
    cartWindow.destroy()
    viewCart()


def buyCommand(cartWindow):
    global cart
    current_time = datetime.datetime.now()
    cartitems = cart.getCartItems()
    file = open(
       "F:\python_project\\a.txt", "a")
    file.write('\n\nDate:-'+str(current_time.date()) +
               '\tTime:-'+str(current_time.time())+'\n')
    for items in cartitems:
        file.write(str(items.name) + '\t' + str(items.price) + '\n')

    price = cart.getTotalPrice()
    file.write('Total_Price   :-   '+str(price)+'\n')
    file.close()
    cart.emptyCart()
    cartWindow.destroy()
    messagebox.showinfo(
        title="success", message="Purchase Completed Successfully")


storeWindow = tk.Tk()
storeWindow.title("The Store")

viewStore()

cart = ShoppingCart()

storeWindow.mainloop()
