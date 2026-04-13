#!/usr/bin/env python3
"""
Login Validation System - Python Implementation
APT1030-A Fundamentals of Programming Languages
"""

def login():
    # Predefined credentials
    VALID_USERNAME = "adminKE"
    VALID_PASSWORD = "254Secure"
    
    print("=" * 40)
    print("   eCitizen Login System")
    print("=" * 40)
    
    # Get user input
    username = input("\nEnter username: ")
    password = input("Enter password: ")
    
    print("\n" + "-" * 40)
    
    # Validate credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        print("✅ Access Granted")
        print(f"Welcome back, {username}!")
    else:
        print("❌ Invalid Credentials")
        print("Please check your username and password.")
    
    print("-" * 40)

if __name__ == "__main__":
    login()