#!/usr/bin/env python3
"""
SACCO Member Financial Record - Python Implementation
Demonstrates Dynamic Typing
APT1030-A Fundamentals of Programming Languages
"""

class SACCOMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.monthly_contributions = []
    
    def add_contribution(self, amount):
        """Add monthly contribution - Python accepts any type"""
        try:
            # Python allows type coercion automatically
            self.monthly_contributions.append(float(amount))
            print(f"✅ Added: KES {float(amount)}")
            return True
        except ValueError:
            print(f"❌ Error: '{amount}' is not a valid number")
            return False
    
    def calculate_total_savings(self):
        """Calculate total savings"""
        return sum(self.monthly_contributions)
    
    def display_record(self):
        """Display member record"""
        print("\n" + "="*50)
        print("SACCO MEMBER RECORD")
        print("="*50)
        print(f"Member ID: {self.member_id}")
        print(f"Member Name: {self.name}")
        print(f"Monthly Contributions: {self.monthly_contributions}")
        print(f"Total Savings: KES {self.calculate_total_savings():,.2f}")
        print("="*50)

def main():
    print("="*50)
    print("   SACCO Member Financial System")
    print("="*50)
    
    # Get member details
    member_id = input("\nEnter Member ID: ")
    name = input("Enter Member Name: ")
    
    # Create member
    member = SACCOMember(member_id, name)
    
    print("\n--- Enter 6 Months of Contributions ---")
    for month in range(1, 7):
        print(f"\nMonth {month}:")
        contribution = input(f"Enter contribution amount (KES): ")
        member.add_contribution(contribution)
    
    # Display record
    member.display_record()
    
    # DEMONSTRATION: Type coercion in Python
    print("\n" + "="*50)
    print("TYPE COERCION DEMONSTRATION")
    print("="*50)
    print("Python automatically handles type conversion:")
    
    # This will work - Python coerces string to float
    test_value = "5000"
    print(f"String '5000' + 1000 = {float(test_value) + 1000}")
    
    # Critical Test: Assigning string to numeric field
    print("\n--- CRITICAL TEST: String Assignment ---")
    print("Attempting to add 'invalid_string' as contribution...")
    member.add_contribution("invalid_string")
    print("Python raises ValueError but program continues!")
    
    member.display_record()

if __name__ == "__main__":
    main()