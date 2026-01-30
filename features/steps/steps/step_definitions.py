from behave import given, when, then
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.number_category import categorize_number

@given('the number is {value}')
def step_given_number_is(context, value):
    context.number = float(value)

@when('I ask for its category')
def step_when_i_ask_category(context):
    context.actual_answer = categorize_number(context.number)

@then('the result should be "{expected_answer}"')
def step_then_should_be_told(context, expected_answer):
    assert context.actual_answer == expected_answer, \
        f"Expected '{expected_answer}', but got '{context.actual_answer}'"