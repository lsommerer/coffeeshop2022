
from toolbox import is_number

class Product(object):

    types = ['coffee', 'tea', 'mugs']

    def __init__(self, name, type, price):
        self._name = str(name).strip()
        if is_number(price):
            self._price = float(price)
        else:
            raise TypeError('Product price must be a numerical type.')
        type = str(type).strip()
        if type in Product.types:
            self._type = type
        else:
            raise TypeError('Product type must be a member of Product.type.')

    def __str__(self):
        return f'{self._name} ({self._type}) ${self._price:0.2f}/lb'

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    name = property(get_name)
    price = property(get_price)
