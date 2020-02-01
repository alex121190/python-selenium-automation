# Created by Alex at 2/1/2020
Feature: Cancel amazon order search

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon main page
    Then Click the help button
    When Search input fill Cancel Items or Orders
    Then Click submit button
    Then Assert Cancel Items or Orders