# You can import a module both ways:
# from sales import calc_shipping
# import sales

from sales import calc_shipping, calc_tax
import sales

sales.calc_tax()

calc_shipping()
calc_tax()
