Feature: Number categorize

  Scenario Outline: Today is or is not Friday
    Given today is "<int>"
    When I ask whether it's Friday yet
    Then I should be told "<answer>"

  Examples:
    | int             | answer |
    | 5         | Pozitív |
    | -3         | Negatív |
    | 0           |  Nulla |