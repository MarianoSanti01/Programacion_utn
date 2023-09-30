from functions.numbers_addition import *
shop_cart={
    "modulo":[12000,25],
    "pin":[500,5],
    "glass":[4000,30]
}
discounts=discount(shop_cart)

print("el precio final de los productos del carrito es",sum(discounts))