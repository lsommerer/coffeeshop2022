from product import Product
from customer import Customer
from shippingmethod import ShippingMethod

class Store(object):

    def __init__(self):
        self._customers = []
        self._products = []
        self.read_products('inventory.txt')
        self._shippingMethods = []
        self.read_shipping_methods('shipping.txt')
        self._currentCustomer = None
        self._currentOrder = None

    def __str__(self):
        """
        Returns a string containing the products, shipping methods and customers of the store.
        """
        pass

    def read_products(self, filename):
        """
        Read the available products from a file, creates Product objects for them, and
        puts them in the product list.
        """
        with open(filename, 'r') as productsFile:
            for line in productsFile:
                name, type, price = line.split(',')
                try:
                    self._products.append(Product(name, type, price))
                except TypeError:
                    print(f'{name} not added to inventory. Check {filename}.')

    def read_shipping_methods(self, filename):
        """
        Read the available products from a file., creates ShippingMethod objects for them,
        and puts them in the shipping methods list.
        """
        pass

    def display_products(self):
        """
        Returns a string of products used to display the products.
        """
        pass

    def display_shipping_methods(self):
        """
        Returns a string of shipping methods used to display the shipping methods .
        """
        pass

    def sales(self):
        """
        Returns the total dollar amount sold today.
        """
        pass

    def shipping(self):
        """
        Returns the total shipping amount today.
        """
        pass

    def tax(self):
        """
        Returns the total tax collected today.
        """
        pass

    def add_customer(self):
        """
        Add a new customer.
        :return: None
        """
        #
        # Check and see if there is a current customer, and deal with it first if necessary.
        #

        #
        # Create a new customer object and make it the current customer.
        #
        self._customers.append(customer)

    def add_order(self):
        """
        Add an order to the current customer.
        :return: None
        """
        #
        # Check to see if there is a customer to add an order to. Create one if not (or error out).
        #

        #
        # Create a new order object and make it the current order.
        #

    def add_item(self):
        """
        Add an item to the current order.
        :return: None
        """
        #
        # Check to see if there is an order to add an item to. Create one if noe (or error out)
        #

        #
        # Create a new lineItem object and add it to the current order
        #

    def print_receipt(self):
        print(self._currentOrder.receipt())

    def get_products(self):
        return self._products

    def get_shipping_methods(self):
        return self._shippingMethods

    def get_customers(self):
        return self._customers

    products = property(get_products)
    shippingMethods = property(get_shipping_methods)
    customers = property(get_customers)

    def run(self):
        commandString = 'ADD: [C]ustomer  [O]rder  [I]tem   PRINT: [R]eciept  [T]otals   [Q]UIT'
        validCommands = 'coirtq'
        finished = False
        while not finished:
            command = get_command(commandString, validCommands)
            if command == 'c':
                self.add_customer()
            elif command == 'o':
                self.add_order()
        #
        # And so forth...
        #