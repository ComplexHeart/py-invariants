Feature: Invariants protect the data integrity.

  Scenario: Cannot instantiate OrderLine due to invariant violation
     Given order line with negative unit price
      When instantiate new OrderLine object
      Then invariants will throw an exception