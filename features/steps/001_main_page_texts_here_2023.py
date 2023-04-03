from behave import *

@given("Loginpage") #1
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Verify text 1 "{text_1}" is here') #2
def text_is_here_1(context, text_1):
    """
    Verify text "THE BEST. THE BRIGHTEST." is here
    """
    context.app.main_page.text_is_here_1(text_1)

@then('Verify text 2 "{text_2}" is here') #3
def text_is_here_2(context, text_2):
    """
    Verify text "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU. LEARN MORE ABOUT US" is here
    """
    context.app.main_page.text_is_here_2(text_2)

@then('Verify button "{text_3}" is in header and click on it') #4
def vrf_btn_hr_clck(context, text_3):
    """
    Verify button "CONTACT US" is in header and click on it
    """
    context.app.main_page.vrf_btn_hr_clck(text_3)

@then('Verify button "{text_4}" is in footer and click on it') #5
def vrf_btn_hr_ftr_clck(context, text_4):
    """
    Verify button "CONTACT US" is in footer and click on it
    """
    context.app.main_page.vrf_btn_hr_ftr_clck(text_4)

@then('Click on "CONTACT US" button in header and verify 1 "{text_5}" is here') #6
def clc_cnct_us_chcg_hr(context, text_5):
    """
    Click on "CONTACT US" button in header and verify 1 "CHICAGO, ILLINOIS 60603" is here
    """
    context.app.main_page.clc_cnct_us_chcg_hr(text_5)

@then('Then Click on "CONTACT US" button in header and verify 2 "{text_6}" is here') #7
def clc_cnct_us_dbln_hr(context, text_6):
    """
    Then Click on "CONTACT US" button in header and verify 2 "DUBLIN 1, IRELAND" is here
    """
    context.app.main_page.clc_cnct_us_dbln_hr(text_6)