/**
 * Ride-Hailing Pricing Engine - Procedural Version
 * Nairobi pricing: Base fare 200 KES + 50 KES per km
 * APT1030-A Fundamentals of Programming Languages
 */

#include <iostream>
#include <iomanip>
using namespace std;

// Constants
const double BASE_FARE = 200.0;
const double COST_PER_KM = 50.0;

// Function to calculate fare
double calculateFare(double distance) {
    return BASE_FARE + (distance * COST_PER_KM);
}

// Function to apply surge pricing
double applySurgePricing(double fare, double surgeMultiplier) {
    return fare * surgeMultiplier;
}

// Function to display fare
void displayFare(double distance, double fare, bool hasSurge = false, double surgeMultiplier = 1.0) {
    cout << "\n========================================" << endl;
    cout << "   RIDE DETAILS" << endl;
    cout << "========================================" << endl;
    cout << "Distance: " << distance << " km" << endl;
    cout << "Base Fare: KES " << BASE_FARE << endl;
    cout << "Rate per km: KES " << COST_PER_KM << endl;
    
    if (hasSurge) {
        cout << "Surge Multiplier: " << surgeMultiplier << "x" << endl;
        cout << "Original Fare: KES " << fixed << setprecision(2) << (fare / surgeMultiplier) << endl;
    }
    
    cout << "----------------------------------------" << endl;
    cout << "TOTAL FARE: KES " << fixed << setprecision(2) << fare << endl;
    cout << "========================================" << endl;
}

// Procedural main function
int main() {
    double distance;
    char hasSurge;
    double surgeMultiplier = 1.0;
    
    cout << "========================================" << endl;
    cout << "   NAIROBI RIDE-HAILING PRICING" << endl;
    cout << "========================================" << endl;
    cout << "\nBase Fare: KES " << BASE_FARE << endl;
    cout << "Cost per km: KES " << COST_PER_KM << endl;
    
    // Get input
    cout << "\nEnter distance (km): ";
    cin >> distance;
    
    cout << "Is surge pricing active? (y/n): ";
    cin >> hasSurge;
    
    if (hasSurge == 'y' || hasSurge == 'Y') {
        cout << "Enter surge multiplier (e.g., 1.5 for 50% increase): ";
        cin >> surgeMultiplier;
    }
    
    // Calculate fare
    double fare = calculateFare(distance);
    
    if (surgeMultiplier != 1.0) {
        fare = applySurgePricing(fare, surgeMultiplier);
        displayFare(distance, fare, true, surgeMultiplier);
    } else {
        displayFare(distance, fare);
    }
    
    // Demonstration of procedural style
    cout << "\n--- Procedural Style Characteristics ---" << endl;
    cout << "✓ Functions operate on data" << endl;
    cout << "✓ No objects/classes" << endl;
    cout << "✓ Data passed between functions" << endl;
    
    return 0;
}