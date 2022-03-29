
from toolbox import is_number

class ShippingMethod(object):

    def __init__(self, name, description, basePrice, pricePerPound):
        self._name = str(name).strip()
        self._description = str(description).strip()
        if is_number(basePrice):
            self._basePrice = float(basePrice)
        else:
            raise TypeError('ShippingMethod basePrice must be a numerical type.')
        if is_number(pricePerPound):
            self._pricePerPound = float(pricePerPound)
        else:
            raise TypeError('ShippingMethod pricePerPound must be a numerical type.')

    def __str__(self):
        string =  f'{self._name} ${self._basePrice:0.2f} + ${self._pricePerPound:0.2f}/lb '
        string += f'({self._description})'
        return string

    def cost(self, amount):
        return self._basePrice + (self._pricePerPound * amount)