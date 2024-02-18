# Created by vadimzemlyanoy at 2/18/24
Feature: Target.com Sign in page

  Scenario: Logged out user can access Sign In
    Given Open Target main page
    When Click Sign In
    When From right side navigation menu, click Sign In
    Then Verify Sign In form opened