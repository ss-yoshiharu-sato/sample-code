import os
import sys
import unittest

from time import sleep
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# get userName, password from Environment variable
RTK_USERNAME = os.environ.get('RTK_USERNAME')
RTK_PASSWORD = os.environ.get('RTK_PASSWORD')
if not RTK_USERNAME or not RTK_PASSWORD:
    print("Environment variable error")
    sys.exit()


class AppiumTest(unittest.TestCase):
    def setUp(self):
        caps = {
            'userName': RTK_USERNAME,
            'password': RTK_PASSWORD,
            'deviceName': 'Nexus 5',
            'platformName': 'Android',
            'browserName': 'Chrome'
        }
        self.driver = webdriver.Remote('https://gwjp.appkitbox.com/wd/hub', caps)
        print(self.driver)

    def tearDown(self):
        self.driver.quit()

    def run_test(self):
        print(self.driver.capabilities['snapshotUrl'])
        driver = self.driver

        ''' put the generated appium code here! '''
        # ------


        # ------


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OpenUrlTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
