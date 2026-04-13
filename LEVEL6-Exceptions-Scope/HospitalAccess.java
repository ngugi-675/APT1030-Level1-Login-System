/**
 * Exception Handling Demonstration - Java
 * Hospital Access Control System with Custom Exceptions
 * APT1030-A Fundamentals of Programming Languages
 */

import java.util.Scanner;

// Custom exception class
class AccessDeniedException extends Exception {
    public AccessDeniedException(String message) {
        super(message);
    }
    
    public AccessDeniedException(String message, Throwable cause) {
        super(message, cause);
    }
}

// Another custom exception for invalid levels
class InvalidAccessLevelException extends Exception {
    public InvalidAccessLevelException(String message) {
        super(message);
    }
}

public class HospitalAccess {
    
    // Method that throws checked exception
    public static boolean checkAccess(String role) throws AccessDeniedException {
        if (role == null || !role.equalsIgnoreCase("Doctor")) {
            throw new AccessDeniedException("Access Denied! Role '" + role + 
                                           "' does not have permission. Only Doctors allowed.");
        }
        System.out.println("✅ Access Granted. Welcome Doctor!");
        return true;
    }
    
    // Method with multiple exceptions
    public static boolean checkAccessWithLevel(String role, int level) 
            throws AccessDeniedException, InvalidAccessLevelException {
        
        if (role == null || !role.equalsIgnoreCase("Doctor")) {
            throw new AccessDeniedException("Role '" + role + "' not authorized");
        }
        
        if (level < 1 || level > 3) {
            throw new InvalidAccessLevelException("Invalid access level: " + level + 
                                                  ". Must be 1, 2, or 3");
        }
        
        switch (level) {
            case 1:
                System.out.println("  Access Level 1: Patient Records Only");
                break;
            case 2:
                System.out.println("  Access Level 2: Patient Records + Prescriptions");
                break;
            case 3:
                System.out.println("  Access Level 3: Full System Access");
                break;
        }
        
        return true;
    }
    
    // Method demonstrating try-catch-finally
    public static void riskyOperation(String value) {
        try {
            int number = Integer.parseInt(value);
            int result = 100 / number;
            System.out.println("  Result: " + result);
        } catch (NumberFormatException e) {
            System.out.println("❌ NumberFormatException: '" + value + 
                             "' cannot be converted to integer");
        } catch (ArithmeticException e) {
            System.out.println("❌ ArithmeticException: Cannot divide by zero");
        } catch (Exception e) {
            System.out.println("❌ Unexpected error: " + e.getMessage());
        } finally {
            System.out.println("  Finally block always executes");
        }
    }
    
    // Method demonstrating try-with-resources (Java 7+)
    public static void readUserInput() {
        // Automatic resource management
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter test value: ");
            String input = scanner.nextLine();
            System.out.println("You entered: " + input);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        // Scanner automatically closed here
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=".repeat(60));
        System.out.println("   HOSPITAL ACCESS CONTROL SYSTEM (JAVA)");
        System.out.println("=".repeat(60));
        
        // Demonstration 1: Basic exception handling
        System.out.println("\n--- Demonstration 1: Basic Access Check ---");
        
        String[] rolesToTest = {"Doctor", "Nurse", "Administrator", "Patient"};
        
        for (String role : rolesToTest) {
            System.out.println("\nAttempting access with role: " + role);
            try {
                checkAccess(role);
            } catch (AccessDeniedException e) {
                System.out.println("❌ " + e.getMessage());
            }
        }
        
        // Demonstration 2: Try-catch-finally
        System.out.println("\n--- Demonstration 2: Try-Catch-Finally ---");
        
        try {
            System.out.print("\nEnter your role (Doctor/Nurse/Admin): ");
            String role = scanner.nextLine();
            checkAccess(role);
        } catch (AccessDeniedException e) {
            System.out.println("❌ Exception caught: " + e.getMessage());
        } finally {
            System.out.println("🔒 Finally block - Always executes!");
        }
        
        // Demonstration 3: Multiple catch blocks
        System.out.println("\n--- Demonstration 3: Multiple Exception Types ---");
        
        String[] testValues = {"10", "0", "abc", "5.5", "100"};
        
        for (String value : testValues) {
            System.out.println("\nProcessing: " + value);
            riskyOperation(value);
        }
        
        // Demonstration 4: Multi-catch (Java 7+)
        System.out.println("\n--- Demonstration 4: Multi-catch Example ---");
        
        try {
            System.out.print("Enter a number: ");
            String input = scanner.nextLine();
            int num = Integer.parseInt(input);
            int result = 100 / num;
            System.out.println("Result: " + result);
        } catch (NumberFormatException | ArithmeticException e) {
            System.out.println("❌ Error: " + e.getClass().getSimpleName() + " - " + e.getMessage());
        }
        
        // Demonstration 5: Throwing exceptions
        System.out.println("\n--- Demonstration 5: Access Level Check ---");
        
        try {
            System.out.print("\nEnter role: ");
            String role = scanner.nextLine();
            System.out.print("Enter access level (1-3): ");
            int level = scanner.nextInt();
            scanner.nextLine(); // Consume newline
            
            checkAccessWithLevel(role, level);
            System.out.println("✅ Access configuration successful!");
            
        } catch (AccessDeniedException e) {
            System.out.println("❌ Access Error: " + e.getMessage());
        } catch (InvalidAccessLevelException e) {
            System.out.println("❌ Level Error: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("❌ Unexpected Error: " + e.getMessage());
        } finally {
            System.out.println("📝 Access attempt logged");
        }
        
        // Exception hierarchy demonstration
        System.out.println("\n--- Java Exception Hierarchy ---");
        System.out.println("Throwable");
        System.out.println("├── Error (unrecoverable)");
        System.out.println("│   ├── OutOfMemoryError");
        System.out.println("│   └── StackOverflowError");
        System.out.println("└── Exception (recoverable)");
        System.out.println("    ├── RuntimeException (unchecked)");
        System.out.println("    │   ├── ArithmeticException");
        System.out.println("    │   ├── NullPointerException");
        System.out.println("    │   └── NumberFormatException");
        System.out.println("    └── Checked Exceptions");
        System.out.println("        ├── IOException");
        System.out.println("        ├── AccessDeniedException (custom)");
        System.out.println("        └── InvalidAccessLevelException (custom)");
        
        scanner.close();
    }
}