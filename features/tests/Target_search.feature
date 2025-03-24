# Created by craig.herring at 3/8/25
Feature: Target search test cases

#  Scenario: User can search for a tea on Target
#    Given Open Target main page
#    When Search for tea
#    Then Verify correct search results shown for tea
#
#  Scenario: User can search for a iPhone on Target
#    Given Open Target main page
#    When Search for iPhone
#    Then Verify correct search results shown for iPhone
#
#  Scenario: User can search for a dress on Target
#    Given Open Target main page
#    When Search for dress
#    Then Verify correct search results shown for dress

  Scenario Outline: User can search for a product on Target
    Given Open Target main page
    When Search for <search_word>
    Then Verify correct search results shown for <search_word>
    Examples:
    |search_word    |
    |tea            |
    |iPhone         |
    |dress          |
    |jacket         |


    Scenario: User can verify that there are at least 10 benefit cells on Target Circle page
    Given Open Target main page
    When Open Target Circle page
    Then Verify that there are at least 10 benefit cells


  Scenario: User can add a product to cart
    Given Open Target main page
    When Search for plates
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)

