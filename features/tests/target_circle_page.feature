# Created by vadimzemlyanoy at 3/3/24
Feature: Target Circle page

  Scenario: User able to see 5 benefit boxes
    Given Open Target Circle page
    When Search the benefit boxes
    Then Verify 5 benefit boxes are shown
