from selenium.webdriver.common.by import By
from POM import ProductPageLocators
from POM import SearchProductLocators, ParfumLocators
from POM import FlaconiLocators
from POM import SalesParfumLocators, InCartProductLocators
from POM import ConfirmATCLocators


class FlaconiPage:
    def __init__(self, driver):
        self.driver = driver
        self.acc = driver.find_element(By.XPATH,FlaconiLocators.accept_btn_css)
        self.login = driver.find_element(By.XPATH,FlaconiLocators.login_icon_xpath)

    def get_accept(self):
        return self.acc

    def get_login(self):
        return self.login


class SearchProductPage:
    def __init__(self,driver):
        self.driver = driver
        self.search= driver.find_element(By.XPATH,SearchProductLocators.search_text_xpath)
        self.search_btn= driver.find_element(By.XPATH,SearchProductLocators.search_btn_xpath)

    def get_search(self):
        return self.search

    def get_searchBtn(self):
        return self.search_btn


class ParfumPage:
    def __init__(self, driver):
        self.driver = driver
        self.nav_to_damen = driver.find_element(By.XPATH,ParfumLocators.navigate_to_damen)
        self.nav_to_sales = driver.find_element(By.XPATH,ParfumLocators.navigate_to_sales)

    def get_navToDamen(self):
        return self.nav_to_damen

    def get_navToSales(self):
        return self.nav_to_sales


class SalesParfumPage:
    def __init__(self, driver):
        self.driver = driver
        self.product = driver.find_element(By.XPATH, SalesParfumLocators.product_sales)

    def get_SaleProd(self):
        return self.product


class ProductPageATC():
    def __init__(self, driver):
        self.driver = driver
        self.addToCart = driver.find_element(By.XPATH, ProductPageLocators.add_to_cart)
        self.productPrice = driver.find_element(By.XPATH, ProductPageLocators.product_price)

    def get_atc(self):
        return self.addToCart

    def get_ProductPrice(self):
        return self.productPrice


class ConfirmAtcPage():
    def __init__(self, driver):
        self.driver = driver

        self.zum_warenkorb = driver.find_element(By.XPATH, ConfirmATCLocators.zum_warenkorb)
        self.weiter_einkaufen = driver.find_element(By.XPATH, ConfirmATCLocators.weiter_einkaufen)

    def get_warenkorb(self):
        return self.zum_warenkorb

    def get_weiterEinkaufen(self):
        return self.weiter_einkaufen


class InCartProductPage():
    def __init__(self, driver):
        self.driver = driver
        self.incart_prod_price = driver.find_element(By.XPATH, InCartProductLocators.prod_price_in_cart)
        self.productName = driver.find_element(By.XPATH, InCartProductLocators.product_name_in_cart)

    def get_InCartProdPrice(self):
        return self.incart_prod_price

    def get_ProductName(self):
        return self.productName

