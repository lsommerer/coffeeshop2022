from lineitem import LineItem

class Order(object):

    def __init__(self, shippingMethod = None, address = None):
        self._address = address
        self._shippingMethod = shippingMethod
        self._lineItems = []

    def __str__(self):
        string = f'address: \n{self._address} \n\nshipping: \n{self._shippingMethod}\n\n'
        string += '    Item                            Cost        Quantity             Total\n'
        string += '--------------------------------------------------------------------------'
        if self._lineItems == []:
            string += '\n   none'
        else:
            for line in self._lineItems:
                string += f'\n   {line}'
        string += '\n--------------------------------------------------------------------------\n'
        string += f'                                                {self.weight():5.2f} lbs         ${self.sales():7.2f}\n\n'
        string += f'                                                         taxes =  ${self.tax():7.2f}\n'
        string += f'                                                      shipping =  ${self.shipping_cost():7.2f}\n'
        string += '                                                               ------------\n'
        string += f'                                                         total =  ${self.total():7.2f}\n'
        return string

    def weight(self):
        orderWeight = 0
        for item in self._lineItems:
            orderWeight += item.amount
        return orderWeight

    def sales(self):
        orderSales = 0
        for item in self._lineItems:
            orderSales += item.total
        return orderSales

    def tax(self):
        return self._address.tax_rate() * self.sales()

    def shipping_cost(self):
        return self._shippingMethod.cost(self.weight())

    def total(self):
        return self.sales() + self.tax() + self.shipping_cost()

    def add(self, product, amount):
        lineItem = LineItem(product, amount)
        self._lineItems.append(lineItem)