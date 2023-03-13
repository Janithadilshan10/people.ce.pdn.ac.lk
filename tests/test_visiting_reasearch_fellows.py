# Author: E/18/098 Ishan Fernando - e18098@eng.pdn.ac.lk
import unittest
import b_webdriver_functions
import a_config_test
import requests
from selenium.webdriver.common.by import By
import json


class Tests(unittest.TestCase):
    def test_if_page_loads(self):
        driver = b_webdriver_functions.getVisitingResearchFellows()
        if driver.page_source.find("Honorary Visiting Research Fellows") == -1:
            self.fail("Honorary Visiting Research Fellows page did not load")

    def test_the_json_is_valid(self):
        with open("../_data/visiting-research-fellows.json") as dataFile:
            json.load(dataFile)

    def test_every_link_in_page(self):
        driver = b_webdriver_functions.getVisitingResearchFellows()
        elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
        # print("Number of links: " + str(len(elems)))
        for elem in elems:
            link = elem.get_attribute("href")
            if a_config_test.SERVER_URL not in link:
                # dont have to test external links
                continue
            thisRequest = requests.get(link)
            self.assertTrue(thisRequest.status_code == 200, link + " is not valid")


if __name__ == "__main__":
    unittest.main()
