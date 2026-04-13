/**
 * Login Validation System - Java Implementation
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.Scanner;

public class LoginValidation {
    
    public static void main(String[] args) {
        // Predefined credentials
        final String VALID_USERNAME = "adminKE";
        final String VALID_PASSWORD = "254Secure";
        
        System.out.println("========================================");
        System.out.println("   eCitizen Login System");
        System.out.println("========================================");
        
        // Get user input
        Scanner scanner = new Scanner(System.in);
        System.out.print("\nEnter username: ");
        String username = scanner.nextLine();
        System.out.print("Enter password: ");
        String password = scanner.nextLine();
        
        System.out.println("\n----------------------------------------");
        
        // Validate credentials
        if (username.equals(VALID_USERNAME) && password.equals(VALID_PASSWORD)) {
            System.out.println("✅ Access Granted");
            System.out.println("Welcome back, " + username + "!");
        } else {
            System.out.println("❌ Invalid Credentials");
            System.out.println("Please check your username and password.");
        }
        
        System.out.println("----------------------------------------");
        scanner.close();
    }
}