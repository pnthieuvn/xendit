# Defined by Hieu Phan at Sep-19, 21
Feature: Verify Calculator canvas functionalities

  Background: Open Calculator Page and Switch to iframe=fullframe
    Given I open Calculator Canvas
    When I switch to iframe=fullframe

  @regression @smoke @single-operator
  Scenario Outline: Verify calculator using single operator: Subtraction, Division, Addition
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value2>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1 | operator      | value2 | expected_result |
#      | 1      | Keys.ADD      | 1      | 2               |
#      | 2      | Keys.ADD      | -3     | -1              |
#      | -2     | Keys.ADD      | -3     | -5              |
#      | 90     | Keys.ADD      | 11     | 101             |
#      |        | Keys.ADD      | 1      | 2               |
#      | 1      | Keys.ADD      |        | 2               |
#      | 1      | Keys.ADD      | a      | 2               |
#      | a      | Keys.ADD      | 1      | 2               |
#      | 100    | Keys.ADD      | 20     | 120             |
#      | 1000   | Keys.ADD      | 20     | 1020            |
#
#      | 1      | Keys.SUBTRACT | 0      | 1               |
#      | 2      | Keys.SUBTRACT | 3     | -1               |
#      | -2     | Keys.SUBTRACT | 3     | -5               |
#      # Failed: somehow, ocr_result: ('19', 85.0)
      | 90     | Keys.SUBTRACT | 11     | 79              |
#      |        | Keys.SUBTRACT | 1      | -1              |
#      # Failed: -ocr_result: ('', 0)
#      | 1      | Keys.SUBTRACT |        | 0               |
#      | a      | Keys.SUBTRACT | 1      | -1              |
#      | 100    | Keys.SUBTRACT | 20     | 80              |
#      | 1000   | Keys.SUBTRACT | 20     | 980             |

#      | 1      | Keys.DIVIDE   | 1      | 1               |
#      | 1      | Keys.DIVIDE   | -1     | 1               |
#      | -1     | Keys.DIVIDE   | -1     | 1               |
#      | 1      | Keys.DIVIDE   | 2      | 0.5             |
#      | 1      | Keys.DIVIDE   | -2     | -0.5            |
#      | 10     | Keys.DIVIDE   | a      | 1               |
#      | a      | Keys.DIVIDE   | 10     | 0               |
#      | 10     | Keys.DIVIDE   |        | 1               |
#      |        | Keys.DIVIDE   | 10     | 0               |
#      | 10     | Keys.DIVIDE   | 0      | Error           |
#      | 0      | Keys.DIVIDE   | 10     | 0               |
#      | 100    | Keys.DIVIDE   | 20     | 50              |
#      | 1000   | Keys.DIVIDE   | 20     | 500              |





  @regression @multiple-operator
  Scenario Outline: Verify calculator using multiple operators: Subtraction, Division, Addition
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<value2>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "<value4>"
    And I enter value into Calculator = "<value5>"
    And I enter value into Calculator = "<value6>"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1        | value2        | value3        | value4        | value5        | value6      | expected_result |
      | 5             | Keys.ADD      | 8             | Keys.DIVIDE   | 2             | Keys.EQUALS | 9               |
      | 5             | Keys.SUBTRACT | 7             | Keys.DIVIDE   | 2             | Keys.EQUALS | 1.5             |
      | 5             | Keys.DIVIDE   | 5             | Keys.SUBTRACT | 6             | Keys.EQUALS | -5              |
      | Keys.ADD      | 5             | Keys.SUBTRACT | Keys.ADD      | 5             | Keys.EQUALS | 10              |
      | Keys.DIVIDE   | 5             | Keys.ADD      | Keys.SUBTRACT | 2             | Keys.EQUALS | -2              |
      | Keys.SUBTRACT | 5             | Keys.DIVIDE   | 2             | Keys.SUBTRACT | Keys.EQUALS | 0               |
      | Keys.ADD      | 5             | Keys.SUBTRACT | -6            | Keys.DIVIDE   | Keys.EQUALS | 4               |
      | Keys.DIVIDE   | 5             | Keys.ADD      | 6             | Keys.SUBTRACT | Keys.EQUALS | 0               |
      | Keys.SUBTRACT | 5             | Keys.EQUALS   | Keys.EQUALS   | Keys.EQUALS   |             | -15             |
      | Keys.ADD      | 5             | Keys.EQUALS   | Keys.EQUALS   | Keys.EQUALS   |             | 15              |
      | 50            | Keys.DIVIDE   | 5             | Keys.EQUALS   | Keys.EQUALS   |             | 2               |

  @regression @data-type
  Scenario Outline: Verify calculator with data type: Float Number, Percentage x Operator
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1 | operator      | value3 | expected_result |
      | 0.1    | Keys.ADD      | 1      | 1.1             |
      | 0.2    | Keys.SUBTRACT | 2      | -1.8            |
      | 0.3    | Keys.DIVIDE   | 3      | 0.1             |
      | 0.4    | Keys.DIVIDE   | 0      | Error           |
      | 50%    | Keys.ADD      | 4      | 4.5             |
      | 60%    | Keys.SUBTRACT | 0.5    | 0.1             |
      | 70%    | Keys.SUBTRACT | 0.8    | -0.1            |
      | 50%    | Keys.DIVIDE   | 5      | 0.1             |

  @regression @boundary
  Scenario Outline: Verify boundary value of Calculator
    When I enter value into Calculator = "<value1>"
    And I enter value into Calculator = "<operator>"
    And I enter value into Calculator = "<value3>"
    And I enter value into Calculator = "Keys.EQUALS"
    Then I should be able to see "<expected_result>"
    And I switch back to default iframe
    Examples:
      | value1      | operator | value3 | expected_result |
      | 12345678    |          | 9      | 123456789       |
      | 123456789   |          | 0      | 123456789       |
      | 999999999   | Keys.ADD | 1      | 1e+9            |
      | -999999999  | Keys.ADD | -1     | -1e+9           |

