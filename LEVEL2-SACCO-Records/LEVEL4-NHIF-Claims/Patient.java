/**
 * Patient Class - NHIF Claims Processing
 * Demonstrates OOP with Encapsulation
 * APT1030-A Fundamentals of Programming Languages
 */

public class Patient {
    // Private fields (encapsulation)
    private String name;
    private String policyNumber;
    private static final double CO_PAYMENT_RATE = 0.10; // 10% co-payment
    
    // Constructor
    public Patient(String name, String policyNumber) {
        this.name = name;
        this.policyNumber = policyNumber;
    }
    
    // Getter methods
    public String getName() {
        return name;
    }
    
    public String getPolicyNumber() {
        return policyNumber;
    }
    
    // Calculate claim after co-payment deduction
    public double calculateClaim(double amount) {
        if (amount < 0) {
            throw new IllegalArgumentException("Amount cannot be negative");
        }
        double coPayment = amount * CO_PAYMENT_RATE;
        return amount - coPayment;
    }
    
    // Calculate co-payment amount
    public double calculateCoPayment(double amount) {
        return amount * CO_PAYMENT_RATE;
    }
    
    // Display claim information
    public void displayClaimInfo(double amount) {
        double coPayment = calculateCoPayment(amount);
        double claimAmount = calculateClaim(amount);
        
        System.out.println("\n" + "=".repeat(50));
        System.out.println("NHIF CLAIM SUMMARY");
        System.out.println("=".repeat(50));
        System.out.println("Patient Name: " + name);
        System.out.println("Policy Number: " + policyNumber);
        System.out.printf("Total Bill: KES %.2f%n", amount);
        System.out.printf("Co-payment (10%%): KES %.2f%n", coPayment);
        System.out.printf("NHIF Coverage: KES %.2f%n", claimAmount);
        System.out.printf("Patient Pays: KES %.2f%n", coPayment);
        System.out.println("=".repeat(50));
    }
}