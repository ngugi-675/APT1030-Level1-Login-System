# Exception Handling & Scope Analysis

## Exception Handling Comparison

### Python vs Java Exceptions

| Aspect | Python | Java |
|--------|--------|------|
| **Exception Hierarchy** | BaseException → Exception → Custom | Throwable → Exception/RuntimeException |
| **Checked Exceptions** | ❌ No (all unchecked) | ✅ Yes (compile-time checking) |
| **Try-Catch-Finally** | ✅ Yes | ✅ Yes |
| **Try-Except-Else** | ✅ Yes (unique to Python) | ❌ No |
| **Custom Exceptions** | ✅ Yes (inherit Exception) | ✅ Yes (extends Exception) |
| **Multi-catch** | ✅ Yes (multiple except blocks) | ✅ Yes (Java 7+ multi-catch) |
| **Try-with-resources** | ✅ Yes (with statement) | ✅ Yes (Java 7+) |

### Python Exception Example
```python
try:
    risky_operation()
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Math error: {e}")
else:
    print("No errors!")  # Runs if no exception
finally:
    print("Always runs")