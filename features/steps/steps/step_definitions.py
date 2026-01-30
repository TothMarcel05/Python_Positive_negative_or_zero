from behave import given, when, then
from src.number_category.py import number_category

@given('today is Friday')
def step_given_today_is(context):
        context.today = "Friday"


@when("I ask whether it's Friday yet")
def step_when_i_ask_whether_its_friday_yet(context):
        context.actual_answer = number_category(context.today)


@then('I should be told "{expected_answer}"')
def step_then_i_should_be_told(context, expected_answer):
        assert context.actual_answer == expected_answer, \
            f"Expected '{expected_answer}', but got '{context.actual_answer}'"



# TODO: Importáld a number_category modult, amikor elkészült



# TODO: Írd meg a step definition-öket a feature fájlban lévő scenáriók alapján

