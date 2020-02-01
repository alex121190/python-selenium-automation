# Created by Alex at 2/1/2020
Feature: Shopping cart is empty
  # Enter feature description here

  Scenario: User can check if shopping cart is empty
    Given Open Amazon page
    Then Click the cart icon
    Then Check that Your Shopping Cart is empty
