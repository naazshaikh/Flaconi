from selenium import webdriver

class Base():
    def launch_browser(self):
        self.driver = webdriver.Chrome(executable_path=r'..\Drivers\chromedriver.exe')
        return self.driver

    def get_url(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click(self,element):
        element.click()

    #insert Value
    def insert_values(self,element, value):
        return element.send_keys(value)

    #Fetch Value
    def get_attribute(self,element,value):
        return element.get_attribute(value)

    def get_text(self,element):
        return element.text

    def nav_back(self):
        self.driver.back()

