# Created by vadimzemlyanoy at 2/3/24
Feature: Target.com search tests

  Scenario: User can search for a product on target
    Given Open Target main page
    When Search for lamp
    Then Search results for lamp are shown
    
Scenario: User can search for a car on target
    Given Open Target main page
    When Search for car
    Then Search results for car are shown