# Programming Paradigm Comparison: Ride-Hailing System

## Overview
Comparison of three programming paradigms implementing the same ride-hailing pricing engine.

## Paradigm Characteristics

| Aspect | Procedural (C++) | OOP (Python/Java) | Functional (Python) |
|--------|-----------------|-------------------|---------------------|
| **Code Organization** | Functions | Classes & Objects | Pure functions |
| **Data Management** | Passed between functions | Encapsulated in objects | Immutable data |
| **State Changes** | Explicit | Through methods | Avoided (no side effects) |
| **Reusability** | Function libraries | Inheritance/Polymorphism | Higher-order functions |
| **Testing** | Easy | Moderate | Very easy (pure functions) |

## Code Comparison

### Procedural (C++)
```cpp
double calculateFare(double distance) {
    return 200 + (distance * 50);
}

double fare = calculateFare(10);