/**
 * NHIF Claims Processing System - Main Class
 * Demonstrates OOP with multiple classes
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.Scanner;
import java.util.ArrayList;

public class NHIFSystem {
    
    private static ArrayList<Patient> patients = new ArrayList<>();
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=".repeat(50));
        System.out.println("   NHIF CLAIMS PROCESSING SYSTEM");
        System.out.println("=".repeat(50));
        
        while (true) {
            System.out.println("\n--- Menu ---");
            System.out.println("1. Add New Patient");
            System.out.println("2. Process Claim");
            System.out.println("3. View All Patients");
            System.out.println("4. Exit");
            System.out.print("\nChoose option: ");
            
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            switch (choice) {
                case 1:
                    addPatient(scanner);
                    break;
                case 2:
                    processClaim(scanner);
                    break;
                case 3:
                    viewAllPatients();
                    break;
                case 4:
                    System.out.println("\nThank you using NHIF System!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid option!");
            }
        }
    }
    
    private static void addPatient(Scanner scanner) {
        System.out.print("\nEnter patient name: ");
        String name = scanner.nextLine();
        System.out.print("Enter policy number: ");
        String policyNumber = scanner.nextLine();
        
        Patient patient = new Patient(name, policyNumber);
        patients.add(patient);
        
        System.out.println("✅ Patient added successfully!");
        System.out.println("   Policy Number: " + policyNumber);
    }
    
    private static void processClaim(Scanner scanner) {
        if (patients.isEmpty()) {
            System.out.println("\n❌ No patients registered!");
            return;
        }
        
        System.out.print("\nEnter policy number: ");
        String policyNumber = scanner.nextLine();
        
        Patient patient = findPatient(policyNumber);
        if (patient == null) {
            System.out.println("❌ Patient not found!");
            return;
        }
        
        System.out.print("Enter claim amount (KES): ");
        double amount = scanner.nextDouble();
        
        patient.displayClaimInfo(amount);
    }
    
    private static void viewAllPatients() {
        if (patients.isEmpty()) {
            System.out.println("\nNo patients registered.");
            return;
        }
        
        System.out.println("\n" + "=".repeat(50));
        System.out.println("REGISTERED PATIENTS");
        System.out.println("=".repeat(50));
        
        for (int i = 0; i < patients.size(); i++) {
            Patient p = patients.get(i);
            System.out.printf("%d. %s (Policy: %s)%n", 
                            i + 1, p.getName(), p.getPolicyNumber());
        }
        System.out.println("=".repeat(50));
    }
    
    private static Patient findPatient(String policyNumber) {
        for (Patient p : patients) {
            if (p.getPolicyNumber().equals(policyNumber)) {
                return p;
            }
        }
        return null;
    }
}