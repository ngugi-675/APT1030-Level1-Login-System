#!/usr/bin/env python3
"""
Ride-Hailing Pricing Engine - Functional Version
Demonstrates functional programming with lambda functions
APT1030-A Fundamentals of Programming Languages
"""

from functools import reduce

# Constants
BASE_FARE = 200.0
COST_PER_KM = 50.0

# Pure functions (no side effects)
def calculate_base_fare(distance):
    """Pure function - output depends only on input"""
    return BASE_FARE + (distance * COST_PER_KM)

def apply_surge(fare, multiplier=1.0):
    """Apply surge pricing to fare"""
    return fare * multiplier

# Lambda functions (anonymous functions)
calculate_fare_lambda = lambda distance, multiplier=1.0: (BASE_FARE + distance * COST_PER_KM) * multiplier

# Higher-order function
def create_pricing_strategy(surge_multiplier=1.0):
    """Returns a pricing function (closure)"""
    def pricing_function(distance):
        return (BASE_FARE + distance * COST_PER_KM) * surge_multiplier
    return pricing_function

# Function composition
def compose(*functions):
    """Compose multiple functions together"""
    def composed(arg):
        result = arg
        for f in reversed(functions):
            result = f(result)
        return result
    return composed

def display_fare(distance, fare, multiplier=1.0):
    """Display fare information"""
    print("\n" + "="*50)
    print("   RIDE DETAILS (FUNCTIONAL VERSION)")
    print("="*50)
    print(f"Distance: {distance} km")
    print(f"Base Fare: KES {BASE_FARE:,.2f}")
    print(f"Rate per km: KES {COST_PER_KM:,.2f}")
    
    if multiplier != 1.0:
        print(f"Surge Multiplier: {multiplier}x")
    
    print("-" * 50)
    print(f"💰 TOTAL FARE: KES {fare:,.2f}")
    print("="*50)

def main():
    """Main program - Functional approach"""
    print("="*50)
    print("   NAIROBI RIDE-HAILING PRICING (FUNCTIONAL)")
    print("="*50)
    print(f"\nBase Fare: KES {BASE_FARE}")
    print(f"Cost per km: KES {COST_PER_KM}")
    
    # Get input
    distance = float(input("\nEnter distance (km): "))
    surge_input = input("Is surge pricing active? (y/n): ").lower()
    
    multiplier = 1.0
    if surge_input == 'y':
        multiplier = float(input("Enter surge multiplier (e.g., 1.5): "))
    
    # Method 1: Regular function call
    base_fare = calculate_base_fare(distance)
    final_fare = apply_surge(base_fare, multiplier)
    
    # Method 2: Lambda function (one-liner)
    fare_lambda = calculate_fare_lambda(distance, multiplier)
    
    # Method 3: Using closure (higher-order function)
    pricing_strategy = create_pricing_strategy(multiplier)
    fare_closure = pricing_strategy(distance)
    
    # Method 4: Function composition
    surge_composed = compose(apply_surge, calculate_base_fare)
    fare_composed = surge_composed(distance) * multiplier
    
    # Display results
    display_fare(distance, final_fare, multiplier)
    
    # Demonstrate different functional approaches
    print("\n--- Functional Programming Characteristics ---")
    print("✓ Pure functions (no side effects)")
    print(f"✓ Lambda function result: KES {fare_lambda:,.2f}")
    print(f"✓ Closure result: KES {fare_closure:,.2f}")
    print(f"✓ Function composition result: KES {fare_composed:,.2f}")
    print("\n--- Benefits of Functional Style ---")
    print("• Immutable data")
    print("• Easy to test (pure functions)")
    print("• Concise code with lambdas")
    print("• Function composition")

if __name__ == "__main__":
    main()