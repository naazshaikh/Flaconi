import time
import unittest
from datetime import datetime
from Base.Base import Base
from POM.Pages.FlaconiPages import *


class TestAddToCart(unittest.TestCase):
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
        print('"Add to cart" test begin', datetime.now())
        print('Start Time', datetime.now())

    def test_addToCart(self):
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

            #Add to cart
            self.b.click(ProductPageATC(self.driver).get_atc())
            time.sleep(2)
            self.b.click(ConfirmAtcPage(self.driver).get_warenkorb())

            print(self.b.get_text(InCartProductPage(self.driver).get_ProductName()) + " is added to cart")

        except:
            print('"Add to cart" test failed.')

    def tearDown(self):
        print('End Time', datetime.now())
        print('"Add to cart" test end', datetime.now())
        print(' ')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


