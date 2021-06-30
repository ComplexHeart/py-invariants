from dataclasses import dataclass
from behave import *

from complexheart.domainmodel import with_invariants, invariant, InvariantViolation


@dataclass
@with_invariants
class OrderLine:
    name: str
    unit_price: float
    quantity: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity

    @invariant
    def quantity_must_be_greater_than_zero(self) -> bool:
        return self.quantity >= 0

    @invariant
    def price_must_be_positive_value(self) -> bool:
        return self.unit_price >= 0

    def total_price(self) -> float:
        return self.unit_price * self.quantity


use_step_matcher("re")


@given("order line with negative unit price")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.order_line = {
        'name': 'nintendo Switch',
        'unit_price': -250.0,
        'quantity': 1
    }


@when("instantiate new OrderLine object")
def step_impl(context):
    try:
        OrderLine(**context.order_line)
        context.invariant_has_raised_an_error = False
    except InvariantViolation:
        context.invariant_has_raised_an_error = True


@then("invariants will throw an exception")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.invariant_has_raised_an_error == True
