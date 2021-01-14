from PyUnit.TestAddToCart import TestAddToCart
from PyUnit.TestNavLinks import TestNavLinks
from PyUnit.TestPriceCheck import TestPriceCheck
import unittest

loader = unittest.TestLoader()

flaconiTestSuite = unittest.TestSuite()

flaconiTestSuite.addTest(TestAddToCart("test_addToCart"))
flaconiTestSuite.addTest(TestPriceCheck("test_priceCheck"))
flaconiTestSuite.addTest(TestNavLinks("test_navLinks"))

unittest.TextTestRunner().run(flaconiTestSuite)
