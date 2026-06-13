# ByteBites Tinker Activity

This is a learning project for ByteBites.

## Getting Started

Project setup and development instructions will go here.

## Activity Summary

The core concept students needed to understand was how to translate a UML class diagram into working Python code by mapping attributes, methods, and relationships such as “Customer places Order” directly into class definitions and method signatures.

Students are most likely to struggle with the distinction between stored and derived attributes. The total field on Order is marked as derived (/) in the diagram, meaning it should be computed on demand using compute_total() rather than stored as an instance variable.

AI was helpful for quickly scaffolding boilerplate code, generating __init__ methods, return types, and a test runner.

To guide a student without giving away the answer, ask them to point to the line in the diagram that justifies each method they write. If they cannot find it, they should question whether the method belongs in the design.
