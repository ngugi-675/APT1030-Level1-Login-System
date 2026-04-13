#!/usr/bin/env python3
"""
NHIF Claims Processing System - OOP Version
Demonstrates Classes, Methods, and Encapsulation
APT1030-A Fundamentals of Programming Languages
"""

class Patient:
    """Patient class with encapsulation"""
    
    CO_PAYMENT_RATE = 0.10  # 10% co-payment (class variable)
    
    def __init__(self, name, policy_number):
        """Constructor - initialize patient data"""
        self.__name = name  # Private attribute (encapsulation)
        self.__policy_number = policy_number  # Private attribute
    
    # Getter methods (properties)
    @property
    def name(self):
        return self.__name
    
    @property
    def policy_number(self):
        return self.__policy_number
    
    def calculate_claim(self, amount):
        """Calculate claim after co-payment deduction"""
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        co_payment = amount * self.CO_PAYMENT_RATE
        return amount - co_payment
    
    def calculate_co_payment(self, amount):
        """Calculate co-payment amount"""
        return amount * self.CO_PAYMENT_RATE
    
    def display_claim_info(self, amount):
        """Display complete claim information"""
        co_payment = self.calculate_co_payment(amount)
        claim_amount = self.calculate_claim(amount)
        
        print("\n" + "="*50)
        print("NHIF CLAIM SUMMARY")
        print("="*50)
        print(f"Patient Name: {self.name}")
        print(f"Policy Number: {self.policy_number}")
        print(f"Total Bill: KES {amount:,.2f}")
        print(f"Co-payment (10%): KES {co_payment:,.2f}")
        print(f"NHIF Coverage: KES {claim_amount:,.2f}")
        print(f"Patient Pays: KES {co_payment:,.2f}")
        print("="*50)


class NHIFSystem:
    """Main system class to manage patients and claims"""
    
    def __init__(self):
        self.patients = []
    
    def add_patient(self, name, policy_number):
        """Add new patient to system"""
        patient = Patient(name, policy_number)
        self.patients.append(patient)
        print(f"\n✅ Patient added successfully!")
        print(f"   Policy Number: {policy_number}")
        return patient
    
    def find_patient(self, policy_number):
        """Find patient by policy number"""
        for patient in self.patients:
            if patient.policy_number == policy_number:
                return patient
        return None
    
    def process_claim(self, policy_number, amount):
        """Process claim for a patient"""
        patient = self.find_patient(policy_number)
        if not patient:
            print("\n❌ Patient not found!")
            return False
        
        patient.display_claim_info(amount)
        return True
    
    def view_all_patients(self):
        """Display all registered patients"""
        if not self.patients:
            print("\nNo patients registered.")
            return
        
        print("\n" + "="*50)
        print("REGISTERED PATIENTS")
        print("="*50)
        for i, patient in enumerate(self.patients, 1):
            print(f"{i}. {patient.name} (Policy: {patient.policy_number})")
        print("="*50)


def main():
    """Main program - OOP approach"""
    system = NHIFSystem()
    
    print("="*50)
    print("   NHIF CLAIMS PROCESSING SYSTEM")
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
            system.add_patient(name, policy_number)
            
        elif choice == '2':
            if not system.patients:
                print("\n❌ No patients registered!")
                continue
            policy_number = input("Enter policy number: ")
            amount = float(input("Enter claim amount (KES): "))
            system.process_claim(policy_number, amount)
            
        elif choice == '3':
            system.view_all_patients()
            
        elif choice == '4':
            print("\nThank you for using NHIF System!")
            break
        
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()