# Created by craig.herring at 3/8/25
Feature: Target search test cases

  Scenario: User can search for a product on Target
    Given Open Target main page
    When Search for coffee
    Then Verify correct search results show
