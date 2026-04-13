/**
 * Login Validation System - C++ Implementation
 * APT1030-A Fundamentals of Programming Languages
 */

#include <iostream>
#include <string>
using namespace std;

int main() {
    // Predefined credentials
    const string VALID_USERNAME = "adminKE";
    const string VALID_PASSWORD = "254Secure";
    
    cout << "========================================" << endl;
    cout << "   eCitizen Login System" << endl;
    cout << "========================================" << endl;
    
    // Get user input
    string username, password;
    cout << "\nEnter username: ";
    cin >> username;
    cout << "Enter password: ";
    cin >> password;
    
    cout << "\n----------------------------------------" << endl;
    
    // Validate credentials
    if (username == VALID_USERNAME && password == VALID_PASSWORD) {
        cout << "✅ Access Granted" << endl;
        cout << "Welcome back, " << username << "!" << endl;
    } else {
        cout << "❌ Invalid Credentials" << endl;
        cout << "Please check your username and password." << endl;
    }
    
    cout << "----------------------------------------" << endl;
    
    return 0;
}