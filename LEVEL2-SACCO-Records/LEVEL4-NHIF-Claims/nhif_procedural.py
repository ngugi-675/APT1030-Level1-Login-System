#!/usr/bin/env python3
"""
NHIF Claims Processing System - Procedural Version
No classes - just functions and data structures
APT1030-A Fundamentals of Programming Languages
"""

# Global data structures (instead of classes)
patients = []  # List of dictionaries

CO_PAYMENT_RATE = 0.10  # 10% co-payment


def calculate_claim(amount):
    """Calculate claim after co-payment deduction"""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    co_payment = amount * CO_PAYMENT_RATE
    return amount - co_payment


def calculate_co_payment(amount):
    """Calculate co-payment amount"""
    return amount * CO_PAYMENT_RATE


def display_claim_info(patient, amount):
    """Display claim information"""
    co_payment = calculate_co_payment(amount)
    claim_amount = calculate_claim(amount)
    
    print("\n" + "="*50)
    print("NHIF CLAIM SUMMARY")
    print("="*50)
    print(f"Patient Name: {patient['name']}")
    print(f"Policy Number: {patient['policy_number']}")
    print(f"Total Bill: KES {amount:,.2f}")
    print(f"Co-payment (10%): KES {co_payment:,.2f}")
    print(f"NHIF Coverage: KES {claim_amount:,.2f}")
    print(f"Patient Pays: KES {co_payment:,.2f}")
    print("="*50)


def add_patient(name, policy_number):
    """Add new patient to system"""
    patient = {
        'name': name,
        'policy_number': policy_number
    }
    patients.append(patient)
    print(f"\n✅ Patient added successfully!")
    print(f"   Policy Number: {policy_number}")
    return patient


def find_patient(policy_number):
    """Find patient by policy number"""
    for patient in patients:
        if patient['policy_number'] == policy_number:
            return patient
    return None


def process_claim(policy_number, amount):
    """Process claim for a patient"""
    patient = find_patient(policy_number)
    if not patient:
        print("\n❌ Patient not found!")
        return False
    
    display_claim_info(patient, amount)
    return True


def view_all_patients():
    """Display all registered patients"""
    if not patients:
        print("\nNo patients registered.")
        return
    
    print("\n" + "="*50)
    print("REGISTERED PATIENTS")
    print("="*50)
    for i, patient in enumerate(patients, 1):
        print(f"{i}. {patient['name']} (Policy: {patient['policy_number']})")
    print("="*50)


def main():
    """Main program - Procedural approach (no classes)"""
    
    print("="*50)
    print("   NHIF CLAIMS PROCESSING SYSTEM (PROCEDURAL)")
    print("="*50)
    
    while True:
        print("\n--- Menu ---")
        print("1. Add New Patient")
        print("2. Process Claim")
        print("3. View All Patients")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            policy_number = input("Enter policy number: ")
            add_patient(name, policy_number)
            
        elif choice == '2':
            if not patients:
                print("\n❌ No patients registered!")
                continue
            policy_number = input("Enter policy number: ")
            amount = float(input("Enter claim amount (KES): "))
            process_claim(policy_number, amount)
            
        elif choice == '3':
            view_all_patients()
            
        elif choice == '4':
            print("\nThank you for using NHIF System!")
            break
        
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()