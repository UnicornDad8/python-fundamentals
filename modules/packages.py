# This are 3 examples of how to import files with the __init__.py
# file and treat them like packages

"""
import ecommerce.sales


ecommerce.sales.calc_shipping()
ecommerce.sales.calc_tax()
"""

"""
from ecommerce.sales import calc_shipping, calc_tax


calc_shipping()
calc_tax()
"""


from ecommerce import sales
sales.calc_shipping()
sales.calc_tax()
