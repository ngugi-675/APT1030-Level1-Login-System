/**
 * Bill Calculator - Control Structures Demonstration
 * Shows Switch and Nested If statements in Java
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.Scanner;

public class BillCalculator {
    
    public static double calculateBill(double units, String customerType, Scanner scanner) {
        double bill = 0;
        double rate = 0;
        
        // Using SWITCH statement for main categories
        switch (customerType.toLowerCase()) {
            case "residential":
                System.out.println("  Category: Residential");
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
                    System.out.printf("  Surcharge (10%%): KES %.2f%n", surcharge);
                }
                break;
                
            case "commercial":
                System.out.println("  Category: Commercial");
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
                    System.out.println("  Note: Minimum charge applied");
                    bill = 1000;
                }
                break;
                
            case "industrial":
                System.out.println("  Category: Industrial");
                if (units <= 500) {
                    rate = 12;
                } else if (units <= 1000) {
                    rate = 18;
                } else {
                    rate = 25;
                }
                
                bill = units * rate;
                
                // Industrial peak hour surcharge
                System.out.print("  Peak hours usage? (yes/no): ");
                String peakHours = scanner.next();
                if (peakHours.equalsIgnoreCase("yes")) {
                    double surcharge = bill * 0.15;
                    bill += surcharge;
                    System.out.printf("  Peak hour surcharge (15%%): KES %.2f%n", surcharge);
                }
                break;
                
            default:
                return -1;
        }
        
        System.out.printf("  Rate applied: KES %.2f/unit%n", rate);
        return bill;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=".repeat(50));
        System.out.println("   KPLC BILL CALCULATOR");
        System.out.println("=".repeat(50));
        System.out.println("\nCustomer Types:");
        System.out.println("  1. residential");
        System.out.println("  2. commercial");
        System.out.println("  3. industrial");
        
        // Get input
        System.out.print("\nEnter customer type: ");
        String customerType = scanner.nextLine();
        System.out.print("Enter units consumed: ");
        double units = scanner.nextDouble();
        
        System.out.println("\n" + "-".repeat(50));
        System.out.println("CALCULATING BILL...");
        System.out.println("-".repeat(50));
        
        // Calculate bill
        double bill = calculateBill(units, customerType, scanner);
        
        if (bill == -1) {
            System.out.println("\n❌ Error: Invalid customer type!");
        } else {
            System.out.println("\n✅ Bill calculated successfully!");
            System.out.println("   Customer Type: " + customerType.substring(0, 1).toUpperCase() + 
                             customerType.substring(1).toLowerCase());
            System.out.printf("   Units consumed: %.2f%n", units);
            System.out.printf("\n💰 TOTAL BILL: KES %.2f%n", bill);
        }
        
        System.out.println("\n" + "=".repeat(50));
        scanner.close();
    }
}