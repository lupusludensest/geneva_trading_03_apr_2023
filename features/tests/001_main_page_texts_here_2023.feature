# Created by rapid at 03 фзк 2023
Feature: # Verify text "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU.
# LEARN MORE ABOUT US
# Expected "INSPIRING INNOVATION.", and got: "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU.
# LEARN MORE ABOUT US"" is here

  Scenario: : # Verify text "INSPIRING INNOVATION...
    Given Loginpage
    Then Verify text 1 "THE BEST. THE BRIGHTEST." is here
    Then Verify text 2 "INSPIRING INNOVATION. INSPIRING PASSION. INSPIRING YOU." is here
    Then Verify button "CONTACT US" is in header and click on it
    Then Verify button "CONTACT US" is in footer and click on it
    Then Click on "CONTACT US" button in header and verify 1 "CHICAGO, ILLINOIS 60603" is here
    And Then Click on "CONTACT US" button in header and verify 2 "DUBLIN 1, IRELAND" is here
