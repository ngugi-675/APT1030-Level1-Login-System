/**
 * Ride-Hailing Pricing Engine - Java OOP Version
 * Demonstrates Object-Oriented Programming in Java
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.Scanner;

class RideHailing {
    // Class constants
    private static final double BASE_FARE = 200.0;
    private static final double COST_PER_KM = 50.0;
    
    // Instance variables
    private double distance;
    private double surgeMultiplier;
    private Double fare;  // Using Double object (can be null)
    
    // Constructor
    public RideHailing(double distance) {
        this(distance, 1.0);
    }
    
    public RideHailing(double distance, double surgeMultiplier) {
        setDistance(distance);
        setSurgeMultiplier(surgeMultiplier);
        this.fare = null;
    }
    
    // Getters and Setters (Encapsulation)
    public double getDistance() {
        return distance;
    }
    
    public void setDistance(double distance) {
        if (distance < 0) {
            throw new IllegalArgumentException("Distance cannot be negative");
        }
        this.distance = distance;
        this.fare = null;  // Reset fare
    }
    
    public double getSurgeMultiplier() {
        return surgeMultiplier;
    }
    
    public void setSurgeMultiplier(double surgeMultiplier) {
        if (surgeMultiplier < 1.0) {
            throw new IllegalArgumentException("Surge multiplier must be at least 1.0");
        }
        this.surgeMultiplier = surgeMultiplier;
        this.fare = null;
    }
    
    // Calculate base fare
    public double calculateBaseFare() {
        return BASE_FARE + (distance * COST_PER_KM);
    }
    
    // Calculate final fare
    public double calculateFare() {
        if (fare == null) {
            double base = calculateBaseFare();
            fare = base * surgeMultiplier;
        }
        return fare;
    }
    
    // Display fare details
    public void displayFare() {
        double fareValue = calculateFare();
        double baseFare = calculateBaseFare();
        
        System.out.println("\n" + "=".repeat(50));
        System.out.println("   RIDE DETAILS (JAVA OOP)");
        System.out.println("=".repeat(50));
        System.out.printf("Distance: %.2f km%n", distance);
        System.out.printf("Base Fare: KES %.2f%n", BASE_FARE);
        System.out.printf("Rate per km: KES %.2f%n", COST_PER_KM);
        
        if (surgeMultiplier != 1.0) {
            System.out.printf("Surge Multiplier: %.1fx%n", surgeMultiplier);
            System.out.printf("Original Fare: KES %.2f%n", baseFare);
        }
        
        System.out.println("-".repeat(50));
        System.out.printf("💰 TOTAL FARE: KES %.2f%n", fareValue);
        System.out.println("=".repeat(50));
    }
}

// Inheritance example
class SurgeRide extends RideHailing {
    public SurgeRide(double distance, double surgeMultiplier) {
        super(distance, surgeMultiplier);
        System.out.println("⚠️  Surge pricing is active!");
    }
}

// Main class
public class RideHailingSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=".repeat(50));
        System.out.println("   NAIROBI RIDE-HAILING PRICING");
        System.out.println("=".repeat(50));
        System.out.printf("\nBase Fare: KES %.2f%n", 200.0);
        System.out.printf("Cost per km: KES %.2f%n", 50.0);
        
        // Get input
        System.out.print("\nEnter distance (km): ");
        double distance = scanner.nextDouble();
        
        System.out.print("Is surge pricing active? (y/n): ");
        String surgeInput = scanner.next();
        
        RideHailing ride;
        if (surgeInput.equalsIgnoreCase("y")) {
            System.out.print("Enter surge multiplier (e.g., 1.5): ");
            double multiplier = scanner.nextDouble();
            ride = new SurgeRide(distance, multiplier);
        } else {
            ride = new RideHailing(distance);
        }
        
        // Display fare
        ride.displayFare();
        
        // Demonstrate OOP features
        System.out.println("\n--- Java OOP Characteristics ---");
        System.out.println("✓ Encapsulation (private fields)");
        System.out.println("✓ Inheritance (SurgeRide extends RideHailing)");
        System.out.println("✓ Constructor overloading");
        System.out.println("✓ Type safety");
        
        scanner.close();
    }
}