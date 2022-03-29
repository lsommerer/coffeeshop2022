class Customer(object):

    def __init__(self, name = None, address = None):
        self._name = name
        self._address = address
        self._orders = []

    def __str__(self):
        string = f'{self._name}\n{self._address}\n\nOrders for {self._name}:'
        if self._orders == []:
            string += '\n   none'
        else:
            for order in self._orders:
                string += f'\n{order}'
        return string

    def add(self, order):
        self._orders.append(order)