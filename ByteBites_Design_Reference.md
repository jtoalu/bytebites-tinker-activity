# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Candidate Classes
- Customer
- Item
- ItemCatalog
- Transaction

## Behavioral Instructions
<!-- Write a short set of instructions guiding how your AI assistant should behave 
when helping with this project — for example, which classes to stay within, 
what complexity to avoid, or any preferences for how suggestions are structured. -->
- Keep all implementation within `Customer`, `Item`, `ItemCatalog`, and `Transaction`.
- Use simple in-memory Python classes and lists. Do not add authentication, databases, APIs, UI code, persistence, or external dependencies.
- Preserve the attributes and method names described in the specification unless a change is necessary.
- Treat `Customer.purchase_history` as an ordered list of completed `Transaction` objects. Do not implement real-user verification or login behavior.
- Preserve insertion order for catalog items, transaction items, and purchase history.
- Make category filtering use exact category matches unless the specification is expanded.
- Validate obvious invalid inputs, such as missing names, non-numeric prices, or negative prices, using clear `TypeError` or `ValueError` exceptions. 
Do not invent restrictive rules for unspecified fields such as popularity-rating ranges.
- Calculate transaction totals from the current item prices. Keep the `float` representation used by the specification and avoid introducing a currency 
or payment system.
- Prefer small, readable methods with type hints and short docstrings. Avoid unnecessary abstractions, inheritance, optimization, or defensive complexity.
- When suggesting changes, explain the affected class, state any assumptions, and include focused examples or tests for normal cases and simple edge cases 
such as an empty catalog or transaction.
- Do not silently change public behavior or add features beyond the client request.
