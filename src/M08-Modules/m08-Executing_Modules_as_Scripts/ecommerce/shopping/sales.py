from ecommerce.customer import contact

# from ..customer import contact


def calc_tax():
    pass


def calc_shipping():
    pass


# Whe a module is executed as a script, the __name__ variable is set to __main__
# If it's imported, the __name__ variable is set to the module name, in this case
# which is ecomerce.shopping.sales
if __name__ == "__main__":
    contact.call_contact()
    calc_shipping()
    calc_tax()
