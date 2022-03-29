from customer import Customer
from lineitem import LineItem
from order import Order
from product import Product
from shippingmethod import ShippingMethod
from address import Address


def test():
    print('\n----product test----')
    product = Product('Bubble Tea', 'tea', 13.50)
    print(product)

    print('\n----shipping method test----')
    shippingMethod = ShippingMethod('FedEX', 'Faster and more expensive', 0.00, 4.65)
    print(shippingMethod)

    print('\n----address test----')
    address = Address('1100 North 56th Street', 'Lincoln', 'NE', '68434')
    print(address)

    print('\n----line item test----')
    lineItem = LineItem(product, 3.5)
    print(lineItem)

    print('\n----order test 1----')
    order = Order(shippingMethod, address)
    print(order)
    print('\n----order test 2----')
    order.add(product, 3.5)
    order.add(product, 1)
    print(order)

    print('\n----customer test 1----')
    name = 'Lloyd Sommerer'
    customer = Customer(name, address)
    print(customer)
    print('\n----customer test 2----')
    customer.add(order)
    print(customer)

test()
