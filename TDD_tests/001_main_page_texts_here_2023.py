from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
TEXT_IS_HERE_1 = EC.presence_of_element_located((By.CSS_SELECTOR, "h2.strikethrough"))
TEXT_IS_HERE_2 = EC.presence_of_element_located((By.XPATH, "(//div[@class='inner'])[2]"))
CONTACT_US_BTN_HDR = EC.presence_of_element_located((By.XPATH, "(//a[text() = 'Contact Us'])[1]"))
CONTACT_US_BTN_FTR = EC.presence_of_element_located((By.XPATH, "(//a[text() = 'Contact Us'])[1]"))
CHICAGO_ADR = EC.presence_of_element_located((By.XPATH, "(//div[@class='section'])[1]"))
DUBLIN_ADR = EC.presence_of_element_located((By.XPATH, "(//div[@class='section'])[3]"))

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://geneva-trading.com/' )

# 2. Verify text "THE BEST. THE BRIGHTEST." is here
expected_text = 'THE BEST. THE BRIGHTEST.'
actual_text = wait.until(TEXT_IS_HERE_1).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}\n" ')

# 3. Verify text "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU. LEARN MORE ABOUT US" is here
expected_text = "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU.\nLEARN MORE ABOUT US"
actual_text = wait.until(TEXT_IS_HERE_2).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

# 4. Verify button "CONTACT US" is in header and click on it
expected_text = "CONTACT US"
actual_text = wait.until(CONTACT_US_BTN_HDR).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

# 5. Verify button "CONTACT US" is in footer and click on it
expected_text = "CONTACT US"
actual_text = wait.until(CONTACT_US_BTN_FTR).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
wait.until(CONTACT_US_BTN_HDR).click()

# 6. Click on "CONTACT US" button in header and verify Chicago and Dublin addresses are here
expected_text = "190 SOUTH LASALLE STREET\nSUITE 1800\nCHICAGO, ILLINOIS 60603"
actual_text = wait.until(CHICAGO_ADR).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
wait.until(CONTACT_US_BTN_FTR).click()

expected_text = "LA TOUCHE HOUSE, 2ND FLOOR\nINTERNATIONAL FINANCIAL SERVICES CENTER\nDUBLIN 1, IRELAND"
actual_text = wait.until(DUBLIN_ADR).text
# print(f'Actual text: {actual_text}')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}"\n')

driver.close()

# Sleep to see what we have
sleep(1)

# Driver quit
driver.quit()

