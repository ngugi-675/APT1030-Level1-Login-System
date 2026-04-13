#!/usr/bin/env python3
"""
Variable Scope Experiment - Python
Demonstrates lexical scoping and variable lifetime
APT1030-A Fundamentals of Programming Languages
"""

# Global variable (module scope)
global_variable = "I am a GLOBAL variable"
another_global = "This is also global"

def function_scope_demo():
    """Demonstrate function scope (local variables)"""
    
    # Local variable - only exists inside this function
    local_variable = "I am a LOCAL variable (inside function)"
    
    print("\n--- INSIDE FUNCTION ---")
    print(f"Inside function - Local variable: {local_variable}")
    print(f"Inside function - Global variable: {global_variable}")
    
    # Modifying global variable (requires global keyword)
    # global global_variable  # Uncomment to modify
    # global_variable = "Modified inside function"
    
    return local_variable

def nested_scope_demo():
    """Demonstrate nested scope (closure)"""
    
    outer_variable = "I am in OUTER function"
    
    def inner_function():
        # Can access outer variable (closure)
        inner_variable = "I am in INNER function"
        print(f"  Inner function sees: {outer_variable}")
        print(f"  Inner function sees: {inner_variable}")
        return inner_variable
    
    print("\n--- NESTED SCOPE ---")
    result = inner_function()
    print(f"Outer function got: {result}")
    
    # This would cause error - inner_variable not accessible here
    # print(inner_variable)
    
    return outer_variable

def scope_experiment_1():
    """Experiment 1: Access local variable outside function"""
    print("\n" + "=" * 60)
    print("EXPERIMENT 1: Local Variable Outside Function")
    print("=" * 60)
    
    def create_local():
        x = "I am local to create_local()"
        print(f"Inside function: {x}")
        return x
    
    result = create_local()
    print(f"Returned value: {result}")
    
    # TRYING TO ACCESS LOCAL VARIABLE DIRECTLY
    print("\nAttempting to access 'x' directly...")
    try:
        print(x)  # This will cause NameError
    except NameError as e:
        print(f"❌ ERROR: {e}")
        print("   'x' only exists inside create_local() function!")
    
    print("\n✅ CONCLUSION: Local variables are NOT accessible outside their function")

def scope_experiment_2():
    """Experiment 2: Global vs Local variables"""
    print("\n" + "=" * 60)
    print("EXPERIMENT 2: Global vs Local Variables")
    print("=" * 60)
    
    # Global variable
    value = "GLOBAL"
    print(f"Initial global value: {value}")
    
    def change_local():
        # This creates a LOCAL variable, doesn't modify global
        value = "LOCAL"
        print(f"Inside function (local): {value}")
    
    def change_global():
        # This modifies the GLOBAL variable
        global value
        value = "MODIFIED GLOBAL"
        print(f"Inside function (global): {value}")
    
    change_local()
    print(f"After change_local(): {value}")
    
    change_global()
    print(f"After change_global(): {value}")

def scope_experiment_3():
    """Experiment 3: Variable lifetime"""
    print("\n" + "=" * 60)
    print("EXPERIMENT 3: Variable Lifetime")
    print("=" * 60)
    
    def create_counter():
        count = 0  # Created when function is called
        
        def increment():
            nonlocal count  # Use nonlocal for nested functions
            count += 1
            return count
        
        return increment
    
    counter = create_counter()
    print(f"Counter 1: {counter()}")  # count is preserved between calls
    print(f"Counter 2: {counter()}")
    print(f"Counter 3: {counter()}")
    
    # The 'count' variable persists due to closure
    print("\n✅ The 'count' variable continues to exist (closure)")

def scope_experiment_4():
    """Experiment 4: LEGB Rule (Local, Enclosing, Global, Built-in)"""
    print("\n" + "=" * 60)
    print("EXPERIMENT 4: LEGB Scope Resolution")
    print("=" * 60)
    
    # Global variable
    name = "Global"
    
    def outer():
        # Enclosing variable
        name = "Enclosing"
        
        def inner():
            # Local variable
            name = "Local"
            print(f"  Local scope: {name}")
            return name
        
        print(f"Enclosing scope: {name}")
        inner()
        return name
    
    print(f"Global scope: {name}")
    outer()
    
    # Built-in scope example
    print(f"\nBuilt-in scope example: {len('Hello')}")  # len() is built-in

def main():
    """Main function running all scope experiments"""
    
    print("=" * 60)
    print("   PYTHON SCOPE EXPERIMENTS")
    print("=" * 60)
    
    # Run experiments
    scope_experiment_1()
    scope_experiment_2()
    scope_experiment_3()
    scope_experiment_4()
    
    # Summary
    print("\n" + "=" * 60)
    print("SCOPE SUMMARY")
    print("=" * 60)
    print("""
    Python Scope Rules (LEGB):
    
    L - Local:     Variables defined inside a function
    E - Enclosing: Variables in enclosing functions (closures)
    G - Global:    Variables defined at module level
    B - Built-in:  Python's built-in names (len, print, etc.)
    
    Key Points:
    ✓ Local variables cannot be accessed outside their function
    ✓ Use 'global' keyword to modify global variables
    ✓ Use 'nonlocal' keyword to modify enclosing variables
    ✓ Variables can have different lifetimes (stack vs closure)
    """)

if __name__ == "__main__":
    main()