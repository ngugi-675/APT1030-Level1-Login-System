# OOP vs Procedural Programming: NHIF Claims System

## Comparison Analysis

### Code Structure Comparison

| Aspect | OOP Version | Procedural Version |
|--------|-------------|---------------------|
| **Lines of Code** | ~150 lines | ~130 lines |
| **Number of Functions** | 8 methods | 7 functions |
| **Data Organization** | Encapsulated in classes | Global dictionaries |
| **Reusability** | High (can extend classes) | Moderate (functions only) |
| **Maintainability** | Excellent | Good |

## OOP Version (Patient Class)

```python
class Patient:
    def __init__(self, name, policy_number):
        self.__name = name
        self.__policy_number = policy_number
    
    def calculate_claim(self, amount):
        return amount - (amount * 0.10)