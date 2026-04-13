#!/usr/bin/env python3
"""
Bill Calculator - Control Structures Demonstration
Shows nested if statements in Python
APT1030-A Fundamentals of Programming Languages
"""

def calculate_bill(units, customer_type):
    """
    Calculate electricity bill based on units consumed and customer type
    Using nested if statements
    """
    # Base rates
    if customer_type == "residential":
        if units <= 100:
            rate = 5
        elif units <= 300:
            rate = 8
        else:
            rate = 12
        
        # Calculate bill
        bill = units * rate
        
        # Apply surcharge if applicable
        if units > 500:
            surcharge = bill * 0.10
            bill += surcharge
            print(f"  Surcharge (10%): KES {surcharge:.2f}")
            
    elif customer_type == "commercial":
        if units <= 200:
            rate = 10
        elif units <= 500:
            rate = 15
        else:
            rate = 20
        
        bill = units * rate
        
        # Commercial minimum charge
        if bill < 1000:
            print(f"  Note: Minimum charge applied")
            bill = 1000
            
    elif customer_type == "industrial":
        if units <= 500:
            rate = 12
        elif units <= 1000:
            rate = 18
        else:
            rate = 25
        
        bill = units * rate
        
        # Industrial peak hour surcharge
        peak_hours = input("  Peak hours usage? (yes/no): ").lower()
        if peak_hours == "yes":
            surcharge = bill * 0.15
            bill += surcharge
            print(f"  Peak hour surcharge (15%): KES {surcharge:.2f}")
    else:
        return None, "Invalid customer type"
    
    return bill, f"KES {bill:.2f} at KES {rate}/unit"

def main():
    print("=" * 50)
    print("   KPLC BILL CALCULATOR")
    print("=" * 50)
    print("\nCustomer Types:")
    print("  1. residential")
    print("  2. commercial")
    print("  3. industrial")
    
    # Get input
    customer_type = input("\nEnter customer type: ").lower()
    units = float(input("Enter units consumed: "))
    
    print("\n" + "-" * 50)
    print("CALCULATING BILL...")
    print("-" * 50)
    
    # Calculate bill using nested if
    bill, message = calculate_bill(units, customer_type)
    
    if bill is None:
        print(f"\n❌ Error: {message}")
    else:
        print(f"\n✅ Bill calculated successfully!")
        print(f"   Customer Type: {customer_type.title()}")
        print(f"   Units consumed: {units}")
        print(f"   {message}")
        print(f"\n💰 TOTAL BILL: KES {bill:.2f}")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    main()