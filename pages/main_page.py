from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from Screenshot import *
import time

# Locators
TEXT_IS_HERE_1 = (By.CSS_SELECTOR, "h2.strikethrough")
TEXT_IS_HERE_2 = (By.XPATH, "(//div[@class='inner'])[2]")
CONTACT_US_BTN_HDR = (By.XPATH, "(//a[text() = 'Contact Us'])[1]")
CONTACT_US_BTN_FTR = (By.XPATH, "(//a[text() = 'Contact Us'])[1]")
CHICAGO_ADR = (By.XPATH, "(//div[@class='section'])[1]")
DUBLIN_ADR = (By.XPATH, "(//div[@class='section'])[3]")

class MainPage(Page):

    # 1 Verify text "THE BEST. THE BRIGHTEST." is here
    def text_is_here_1(self, txt):
        self.verify_text(txt, *TEXT_IS_HERE_1)

    # 2 Verify text 2 "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU." is here
    def text_is_here_2(self, txt):
        self.verify_text(txt, *TEXT_IS_HERE_2)

    # 3 Verify button "CONTACT US" is in header and click on it
    def vrf_btn_hr_clck(self, txt):
        self.verify_text(txt, *CONTACT_US_BTN_HDR)
        self.click(*CONTACT_US_BTN_HDR)

    # 4 Verify button "CONTACT US" is in footer and click on it
    def vrf_btn_hr_ftr_clck(self, txt):
        self.verify_text(txt, *CONTACT_US_BTN_FTR)
        self.click(*CONTACT_US_BTN_FTR)

    # 5 Click on "CONTACT US" button in header and verify "CHICAGO, ILLINOIS 60603" and "DUBLIN 1, IRELAND" addresses are here
    def clc_cnct_us_chcg_hr(self, txt):
        self.verify_text(txt, *CHICAGO_ADR)
        self.click(*CONTACT_US_BTN_FTR)

    # 6 Then Click on "CONTACT US" button in header and verify "DUBLIN 1, IRELAND" is here
    def clc_cnct_us_dbln_hr(self, txt):
        self.verify_text(txt, *DUBLIN_ADR)


    # End of the above code
