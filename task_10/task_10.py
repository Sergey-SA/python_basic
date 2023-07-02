from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Keys
import unittest


class Source(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome()
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element(value='APjFqb')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        sleep(2)

        elm = self.drv.find_element(By.XPATH, ('/html/body/div[6]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite'))
        assert 'selenide.org' in elm.text

        elm = self.drv.find_element(By.XPATH, ('/html/body/div[6]/div/div[5]/div/div/div[1]/div[1]/div/a[1]'))
        elm.click()
        elm = self.drv.find_element(By.XPATH, ('/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/h3'))
        assert 'selenide' in elm.text.lower()

        elm = self.drv.find_element(By.XPATH, ('/html/body/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]'))
        elm.click()
        sleep(4)
        elm = self.drv.find_element(By.XPATH, ('/html/body/div[6]/div/div[13]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/div/div/div/cite'))
        assert 'selenide.org' in elm.text

    def tearDown(self):
        self.drv.close()

if __name__ == '__main__':
    unittest.main()


