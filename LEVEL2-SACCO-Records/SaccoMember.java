/**
 * SACCO Member Financial Record - Java Implementation
 * Demonstrates Static Typing
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.ArrayList;
import java.util.Scanner;

class SaccoMember {
    private String memberId;
    private String name;
    private ArrayList<Double> monthlyContributions;
    
    public SaccoMember(String memberId, String name) {
        this.memberId = memberId;
        this.name = name;
        this.monthlyContributions = new ArrayList<>();
    }
    
    public boolean addContribution(double amount) {
        /** Add monthly contribution - Java requires double type */
        monthlyContributions.add(amount);
        System.out.printf("✅ Added: KES %.2f%n", amount);
        return true;
    }
    
    public double calculateTotalSavings() {
        double total = 0;
        for (double contribution : monthlyContributions) {
            total += contribution;
        }
        return total;
    }
    
    public void displayRecord() {
        System.out.println("\n" + "=".repeat(50));
        System.out.println("SACCO MEMBER RECORD");
        System.out.println("=".repeat(50));
        System.out.println("Member ID: " + memberId);
        System.out.println("Member Name: " + name);
        System.out.println("Monthly Contributions: " + monthlyContributions);
        System.out.printf("Total Savings: KES %.2f%n", calculateTotalSavings());
        System.out.println("=".repeat(50));
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=".repeat(50));
        System.out.println("   SACCO Member Financial System");
        System.out.println("=".repeat(50));
        
        // Get member details
        System.out.print("\nEnter Member ID: ");
        String memberId = scanner.nextLine();
        System.out.print("Enter Member Name: ");
        String name = scanner.nextLine();
        
        // Create member
        SaccoMember member = new SaccoMember(memberId, name);
        
        System.out.println("\n--- Enter 6 Months of Contributions ---");
        for (int month = 1; month <= 6; month++) {
            System.out.printf("\nMonth %d:%n", month);
            System.out.print("Enter contribution amount (KES): ");
            double contribution = scanner.nextDouble();
            member.addContribution(contribution);
        }
        
        // Display record
        member.displayRecord();
        
        // DEMONSTRATION: Type coercion in Java
        System.out.println("\n" + "=".repeat(50));
        System.out.println("TYPE COERCION DEMONSTRATION");
        System.out.println("=".repeat(50));
        System.out.println("Java requires explicit type conversion:");
        
        // This would cause COMPILATION ERROR:
        // String testValue = "5000";
        // double result = testValue + 1000;  // COMPILE ERROR!
        
        // Correct way - explicit parsing:
        String testValue = "5000";
        double result = Double.parseDouble(testValue) + 1000;
        System.out.printf("Double.parseDouble('5000') + 1000 = %.2f%n", result);
        
        // Critical Test: Assigning string to double
        System.out.println("\n--- CRITICAL TEST: String Assignment ---");
        System.out.println("Attempting to pass string to addContribution()...");
        System.out.println("❌ Java: COMPILATION ERROR - incompatible types");
        System.out.println("The program wouldn't even compile!");
        System.out.println("String cannot be converted to double");
        
        scanner.close();
    }
}