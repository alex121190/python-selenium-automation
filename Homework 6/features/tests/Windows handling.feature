# Created by Alex at 28.02.2020
Feature: After switching the windows the item doesnt's disappear
  # Enter feature description here

  Scenario: Can switch the windows without losing the item in the cart
    # Enter steps here

  Given Open amazon page
    When Store original windows
    Then Click the Deals link
    Then Switch to the newly opened window
    Then Look up for men shirts
    Then Click search
    When Open first item
    Then Add it to the cart
    Then User can switch back to original
    Then Refresh original window