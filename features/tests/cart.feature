# Created by craig.herring at 3/21/25
Feature: cart tests

    Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown