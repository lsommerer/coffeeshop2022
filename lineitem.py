class LineItem(object):

    def __init__(self, product, amount):
        self._product = product
        if amount > 0:
            self._amount = amount
        else:
            raise ValueError('Amount must be greater than zero.')
        self._total = product.price * amount

    def __str__(self):
        return f'{self._product.name:30s} ${self._product.price:0.2f}/lb   x {self._amount:5.2f} lbs    =    ${self._total:7.2f}'

    def get_total(self):
        return self._total

    total = property(get_total)

    def get_amount(self):
        return self._amount

    amount = property(get_amount)