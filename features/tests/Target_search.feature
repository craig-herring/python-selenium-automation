# Created by craig.herring at 3/8/25
Feature: Target search test cases

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for coffee
    Then Verify correct search results show

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

  Scenario: Logged out user can navigate to Sign In
    Given Open Target main page
    When Click Sign In
    Then Click Sign In from side navigation menu
    Then Verify Sign In form opened