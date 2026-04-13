# Control Structures Comparison: Python vs Java vs C++

## Readability Analysis

### Nested If Statements

**Python:**
```python
if customer_type == "residential":
    if units <= 100:
        rate = 5
    elif units <= 300:
        rate = 8
    else:
        rate = 12