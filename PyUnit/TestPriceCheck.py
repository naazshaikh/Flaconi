import time
import unittest
from datetime import datetime
from Base.Base import Base
from POM.Pages.FlaconiPages import *
import re as regex


class TestPriceCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.b = Base()
            cls.driver = cls.b.launch_browser()
            cls.b.get_url('https://www.flaconi.de/')
            cls.fp = FlaconiPage(cls.driver)
            cls.b.click(cls.fp.get_accept())
            time.sleep(2)
        except:
            print("Failed to open flaconi.de")

    def setUp(self):
        print(' ')
        print('"Price check" test begin', datetime.now())
        print('Start Time', datetime.now())

    def test_priceCheck(self):
        try:
            spp = SearchProductPage(self.driver)
            self.b.insert_values(spp.get_search(), "parfum")
            self.b.click(spp.get_searchBtn())

            ##Navigate
            self.b.click(ParfumPage(self.driver).get_navToDamen())
            self.b.nav_back()
            self.b.click(ParfumPage(self.driver).get_navToSales())
            self.driver.execute_script("arguments[0].scrollIntoView(true)", SalesParfumPage(self.driver).get_SaleProd())
            self.b.click(SalesParfumPage(self.driver).get_SaleProd())

            item_price = regex.sub('[^0-9,]', '', ProductPageATC(self.driver).get_ProductPrice().text)

            self.b.click(ProductPageATC(self.driver).get_atc())
            time.sleep(2)
            self.b.click(ConfirmAtcPage(self.driver).get_warenkorb())

            item_price_in_cart = regex.sub('[^0-9,]', '', InCartProductPage(self.driver).get_InCartProdPrice().text)

            if item_price == item_price_in_cart:
                print("Pass : Price of item on product page and in cart is matching.")
            else:
                print("Failed : Price of item on product page and in cart is not matching.")
        except:
            print('"Price check" test failed')

    def tearDown(self):
        print('End Time', datetime.now())
        print('"Price check" test end', datetime.now())
        print(' ')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
