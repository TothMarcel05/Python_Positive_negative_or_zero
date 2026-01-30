Feature: Number categorization
  As a user
  I want to know if a number is positive, negative, or zero
  So that I can make decisions based on its value

  Scenario Outline: Categorizing various numbers
    Given the number is <value>
    When I ask for its category
    Then the result should be "<answer>"

    Examples:
      | value | answer  |
      | 5     | Pozitív |
      | 100   | Pozitív |
      | -3    | Negatív |
      | -10.5 | Negatív |
      | 0     | Nulla   |
      | 3.14  | Pozitív |
      | 99999 | Pozitív |