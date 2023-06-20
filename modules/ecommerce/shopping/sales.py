from ecommerce.customer import contact
# from ..customer import contact

contact.contact_costumer()

print("Sales initialized", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


# using it as a script only when executing from this file
if __name__ == "__main__":
    print("Sales started")
    calc_tax()
