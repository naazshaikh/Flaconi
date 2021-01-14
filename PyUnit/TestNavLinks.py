import unittest
import time
from datetime import datetime
from pip._vendor import requests
from Base.Base import Base
from POM.Pages.FlaconiPages import *


class TestNavLinks(unittest.TestCase):
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
        print('"Main Navigation Menu Links" test begin', datetime.now())
        print('Start Time', datetime.now())

    def test_navLinks(self):
        try:
            main_nav = self.driver.find_elements_by_xpath("//nav[@id='main-navigation']/ul/li/a")
            number_of_nav_items = len(main_nav)
            print(number_of_nav_items,"main navigation menu links found.")

            for item in range(0, number_of_nav_items):
                print(' ')
                main_nav = self.driver.find_elements_by_xpath("//nav[@id='main-navigation']/ul/li/a")
                print("Menu : " + main_nav[item].text)
                url = main_nav[item].get_attribute("href")
                print("link : " + url)
                if url.strip() == "":
                    print("Type : Empty url.")
                else:
                    if url.startswith("https://www.flaconi.de/"):
                        print("Type : Internal link.")
                    else:
                        print ("Type : External link.")

                    main_nav[item].click()
                    time.sleep(2)

                    print("URL after navigation : " + self.driver.current_url)

                    if url == self.driver.current_url:
                        print("Both Menu link URL and navigated URL are same. No redirection.")
                    else:
                        print("Both Menu link URL and navigated URL are not same. Possible redirection.")

                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            print("Status : Menu link URL is up and running. Returning HTTP 200 code.")
                        else:
                            print("Status : Menu link URL may not be up and returning HTTP " + response.status_code)
                    except:
                        print("Status : Failed to check the URL status.")

                    print(' ')
        except:
            print('"Main Navigation Menu Links" test failed.')

    def tearDown(self):
        print('End Time', datetime.now())
        print('"Main Navigation Menu Links" test end', datetime.now())
        print(' ')

    @classmethod
    def tearDownClass(cls):
        print('')
        cls.driver.close()

