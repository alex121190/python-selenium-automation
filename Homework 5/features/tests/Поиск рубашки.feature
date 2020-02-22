# Created by Alex at 2/19/2020
Feature: Проверить что выбран нужный цвет рубашки
  # Enter feature description here

  Scenario: Находим определенный цвет и добавляем его в корзину
    Given Open Amazon page 1
    When Input men shirts into field
    Then Click search
    Then Choose first result
    Then Get all colors
    Then Add Palm Leaf shirt to the cart
