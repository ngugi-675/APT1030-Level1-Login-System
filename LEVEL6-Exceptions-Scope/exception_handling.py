#!/usr/bin/env python3
"""
Exception Handling Demonstration - Python
Hospital Access Control System
APT1030-A Fundamentals of Programming Languages
"""

# Custom exception for access control
class AccessDeniedError(Exception):
    """Custom exception for access control violations"""
    pass

def checkAccess(role):
    """
    Check if role has access to hospital system
    Raises AccessDeniedError if role is not "Doctor"
    """
    if role != "Doctor":
        raise AccessDeniedError(f"Access Denied! Role '{role}' does not have permission. Only Doctors allowed.")
    else:
        print(f"✅ Access Granted. Welcome Doctor!")
        return True

def checkAccessWithLevel(role, access_level):
    """
    Advanced access check with levels
    Demonstrates multiple exception types
    """
    if role != "Doctor":
        raise AccessDeniedError(f"Role '{role}' not authorized")
    
    if access_level not in [1, 2, 3]:
        raise ValueError(f"Invalid access level: {access_level}. Must be 1, 2, or 3")
    
    if access_level == 1:
        print("  Access Level 1: Patient Records Only")
    elif access_level == 2:
        print("  Access Level 2: Patient Records + Prescriptions")
    elif access_level == 3:
        print("  Access Level 3: Full System Access")
    
    return True

def risky_operation(value):
    """Demonstrate multiple exception types"""
    try:
        # Multiple operations that can raise different exceptions
        number = int(value)  # Could raise ValueError
        result = 100 / number  # Could raise ZeroDivisionError
        return result
    except ValueError:
        print(f"❌ ValueError: '{value}' cannot be converted to integer")
        return None
    except ZeroDivisionError:
        print(f"❌ ZeroDivisionError: Cannot divide by zero")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def main():
    """Main function demonstrating exception handling"""
    
    print("=" * 60)
    print("   HOSPITAL ACCESS CONTROL SYSTEM (PYTHON)")
    print("=" * 60)
    
    # Demonstration 1: Basic exception handling
    print("\n--- Demonstration 1: Basic Access Check ---")
    
    roles_to_test = ["Doctor", "Nurse", "Administrator", "Patient"]
    
    for role in roles_to_test:
        print(f"\nAttempting access with role: {role}")
        try:
            checkAccess(role)
        except AccessDeniedError as e:
            print(f"❌ {e}")
    
    # Demonstration 2: Try-Except-Else-Finally
    print("\n--- Demonstration 2: Try-Except-Else-Finally ---")
    
    try:
        role = input("\nEnter your role (Doctor/Nurse/Admin): ")
        checkAccess(role)
    except AccessDeniedError as e:
        print(f"❌ Exception caught: {e}")
    else:
        print("✅ No exceptions occurred! Access granted.")
    finally:
        print("🔒 This block ALWAYS executes (logging access attempt)")
    
    # Demonstration 3: Multiple exception types
    print("\n--- Demonstration 3: Multiple Exception Types ---")
    
    test_values = ["10", "0", "abc", "5.5", "100"]
    
    for value in test_values:
        print(f"\nProcessing: {value}")
        result = risky_operation(value)
        if result is not None:
            print(f"  Result: {result}")
    
    # Demonstration 4: Exception with else clause
    print("\n--- Demonstration 4: Access Level Check ---")
    
    try:
        role = input("\nEnter role: ")
        level = int(input("Enter access level (1-3): "))
        checkAccessWithLevel(role, level)
    except AccessDeniedError as e:
        print(f"❌ Access Error: {e}")
    except ValueError as e:
        print(f"❌ Value Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
    else:
        print("✅ Access configuration successful!")
    finally:
        print("📝 Access attempt logged")
    
    # Exception hierarchy demonstration
    print("\n--- Exception Hierarchy ---")
    print("BaseException")
    print("├── SystemExit")
    print("├── KeyboardInterrupt")
    print("└── Exception")
    print("    ├── AccessDeniedError (custom)")
    print("    ├── ValueError")
    print("    ├── ZeroDivisionError")
    print("    └── ...")

if __name__ == "__main__":
    main()