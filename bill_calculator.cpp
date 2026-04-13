/**
 * Bill Calculator - Control Structures Demonstration
 * Shows Switch and Nested If statements in C++
 * APT1030-A Fundamentals of Programming Languages
 */

#include <iostream>
#include <string>
#include <cctype>
using namespace std;

double calculateBill(double units, string customerType) {
    double bill = 0;
    double rate = 0;
    
    // Convert to lowercase for comparison
    for (char &c : customerType) {
        c = tolower(c);
    }
    
    // Using SWITCH statement (C++ switch works with integers/enums)
    // For string comparison, we use if-else chain with string comparison
    if (customerType == "residential") {
        cout << "  Category: Residential" << endl;
        
        // Nested if for tiered pricing
        if (units <= 100) {
            rate = 5;
        } else if (units <= 300) {
            rate = 8;
        } else {
            rate = 12;
        }
        
        bill = units * rate;
        
        // Nested if for surcharge
        if (units > 500) {
            double surcharge = bill * 0.10;
            bill += surcharge;
            printf("  Surcharge (10%%): KES %.2f\n", surcharge);
        }
        
    } else if (customerType == "commercial") {
        cout << "  Category: Commercial" << endl;
        
        if (units <= 200) {
            rate = 10;
        } else if (units <= 500) {
            rate = 15;
        } else {
            rate = 20;
        }
        
        bill = units * rate;
        
        // Commercial minimum charge
        if (bill < 1000) {
            cout << "  Note: Minimum charge applied" << endl;
            bill = 1000;
        }
        
    } else if (customerType == "industrial") {
        cout << "  Category: Industrial" << endl;
        
        if (units <= 500) {
            rate = 12;
        } else if (units <= 1000) {
            rate = 18;
        } else {
            rate = 25;
        }
        
        bill = units * rate;
        
        // Industrial peak hour surcharge
        string peakHours;
        cout << "  Peak hours usage? (yes/no): ";
        cin >> peakHours;
        
        if (peakHours == "yes") {
            double surcharge = bill * 0.15;
            bill += surcharge;
            printf("  Peak hour surcharge (15%%): KES %.2f\n", surcharge);
        }
        
    } else {
        return -1;
    }
    
    printf("  Rate applied: KES %.2f/unit\n", rate);
    return bill;
}

int main() {
    string customerType;
    double units;
    
    cout << "================================================" << endl;
    cout << "   KPLC BILL CALCULATOR" << endl;
    cout << "================================================" << endl;
    cout << "\nCustomer Types:" << endl;
    cout << "  1. residential" << endl;
    cout << "  2. commercial" << endl;
    cout << "  3. industrial" << endl;
    
    // Get input
    cout << "\nEnter customer type: ";
    cin >> customerType;
    cout << "Enter units consumed: ";
    cin >> units;
    
    cout << "\n------------------------------------------------" << endl;
    cout << "CALCULATING BILL..." << endl;
    cout << "------------------------------------------------" << endl;
    
    // Calculate bill
    double bill = calculateBill(units, customerType);
    
    if (bill == -1) {
        cout << "\n❌ Error: Invalid customer type!" << endl;
    } else {
        cout << "\n✅ Bill calculated successfully!" << endl;
        cout << "   Customer Type: " << customerType << endl;
        printf("   Units consumed: %.2f\n", units);
        printf("\n💰 TOTAL BILL: KES %.2f\n", bill);
    }
    
    cout << "\n================================================" << endl;
    
    return 0;
}