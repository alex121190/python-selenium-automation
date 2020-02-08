# Created by Alex at 2/7/2020
Feature: Check how many history books Amazon shows us
  # Enter feature description here

  Scenario: Check for history books in Amazon
    Given Open main amazon page
    When In the search field write history books
    Then Click search button
    Then Count how many books would be shown in result list
#    When Find the last book
#    Then Check if the price more that 10$ - add it to cart