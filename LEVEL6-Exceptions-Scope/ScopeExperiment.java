/**
 * Variable Scope Experiment - Java
 * Demonstrates lexical scoping and variable lifetime
 * APT1030-A Fundamentals of Programming Languages
 */

public class ScopeExperiment {
    
    // Class-level (instance) variables
    private String instanceVariable = "I am an INSTANCE variable";
    
    // Static (class) variables
    private static String staticVariable = "I am a STATIC variable";
    private static String globalVariable = "I am like a GLOBAL variable";
    
    // Method 1: Demonstrate local scope
    public void demonstrateLocalScope() {
        // Local variable - only exists inside this method
        String localVariable = "I am a LOCAL variable (inside method)";
        
        System.out.println("\n--- INSIDE METHOD ---");
        System.out.println("Local variable: " + localVariable);
        System.out.println("Instance variable: " + instanceVariable);
        System.out.println("Static variable: " + staticVariable);
        
        // localVariable cannot be accessed outside this method
    }
    
    // Method 2: Block scope (within braces)
    public void demonstrateBlockScope() {
        System.out.println("\n--- BLOCK SCOPE ---");
        
        // Variable in outer block
        int x = 10;
        System.out.println("Outer block x = " + x);
        
        if (x > 5) {
            // Variable in inner block
            int y = 20;
            System.out.println("Inner block y = " + y);
            System.out.println("Inner block can access x = " + x);
            
            // y only exists inside this if block
        }
        
        // This would cause error - y not accessible here
        // System.out.println(y);
        
        System.out.println("After block, y is gone (out of scope)");
    }
    
    // Method 3: Loop scope
    public void demonstrateLoopScope() {
        System.out.println("\n--- LOOP SCOPE ---");
        
        // Variable declared before loop (exists after loop)
        int sum = 0;
        
        for (int i = 0; i < 5; i++) {
            sum += i;
            System.out.println("  Loop iteration " + i + ", sum = " + sum);
        }
        
        System.out.println("After loop, sum = " + sum);
        // i is NOT accessible here (scope limited to loop)
        // System.out.println(i); // ERROR!
    }
    
    // Method 4: Parameter scope
    public void demonstrateParameterScope(String parameter) {
        System.out.println("\n--- PARAMETER SCOPE ---");
        System.out.println("Parameter value: " + parameter);
        
        // Parameter acts like a local variable
        parameter = "Modified inside method";
        System.out.println("Modified parameter: " + parameter);
    }
    
    // Method 5: Shadowing (local variable hides class variable)
    public void demonstrateShadowing() {
        System.out.println("\n--- SHADOWING ---");
        
        // Instance variable
        String instanceVariable = "LOCAL version (shadows instance)";
        
        System.out.println("Local variable: " + instanceVariable);
        System.out.println("Instance variable (use 'this'): " + this.instanceVariable);
    }
    
    // Method 6: Static vs Instance context
    public static void demonstrateStaticContext() {
        System.out.println("\n--- STATIC CONTEXT ---");
        
        // Can access static variables directly
        System.out.println("Static variable: " + staticVariable);
        
        // Cannot access instance variables directly in static method
        // System.out.println(instanceVariable); // ERROR!
        
        // Must create object to access instance variables
        ScopeExperiment obj = new ScopeExperiment();
        System.out.println("Instance variable via object: " + obj.instanceVariable);
    }
    
    // Experiment 1: Access local variable outside method
    public static void experiment1() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("EXPERIMENT 1: Local Variable Outside Method");
        System.out.println("=".repeat(60));
        
        class LocalDemo {
            public String createLocal() {
                String localVar = "I am local to createLocal()";
                System.out.println("Inside method: " + localVar);
                return localVar;
            }
        }
        
        LocalDemo demo = new LocalDemo();
        String result = demo.createLocal();
        System.out.println("Returned value: " + result);
        
        // localVar is NOT accessible here
        System.out.println("\n❌ 'localVar' is not accessible outside createLocal()");
        System.out.println("   Java uses lexical (static) scope");
    }
    
    // Experiment 2: Variable lifetime
    public static void experiment2() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("EXPERIMENT 2: Variable Lifetime");
        System.out.println("=".repeat(60));
        
        // Local variable - created on stack
        int stackVar = 100;
        System.out.println("Stack variable (local): " + stackVar);
        
        // Object - created on heap
        StringBuilder heapVar = new StringBuilder("Heap object");
        System.out.println("Heap variable (object): " + heapVar);
        
        System.out.println("\nVariable Lifetime:");
        System.out.println("  • Stack variables: Exist only within their scope (method/block)");
        System.out.println("  • Heap objects: Exist as long as referenced");
        System.out.println("  • Static variables: Exist for entire program lifetime");
    }
    
    // Experiment 3: Class scope
    public static void experiment3() {
        System.out.println("\n" + "=".repeat(60));
        System.out.println("EXPERIMENT 3: Class Scope");
        System.out.println("=".repeat(60));
        
        ScopeExperiment obj1 = new ScopeExperiment();
        ScopeExperiment obj2 = new ScopeExperiment();
        
        // Each object has its own instance variable
        obj1.instanceVariable = "Object 1's value";
        obj2.instanceVariable = "Object 2's value";
        
        System.out.println("obj1.instanceVariable = " + obj1.instanceVariable);
        System.out.println("obj2.instanceVariable = " + obj2.instanceVariable);
        
        // Static variable is shared across all instances
        staticVariable = "Shared across ALL objects";
        System.out.println("\nStatic variable (shared): " + staticVariable);
        System.out.println("obj1 sees: " + obj1.staticVariable);
        System.out.println("obj2 sees: " + obj2.staticVariable);
    }
    
    public static void main(String[] args) {
        System.out.println("=".repeat(60));
        System.out.println("   JAVA SCOPE EXPERIMENTS");
        System.out.println("=".repeat(60));
        
        ScopeExperiment demo = new ScopeExperiment();
        
        // Run experiments
        demo.demonstrateLocalScope();
        demo.demonstrateBlockScope();
        demo.demonstrateLoopScope();
        demo.demonstrateParameterScope("Test Parameter");
        demo.demonstrateShadowing();
        demonstrateStaticContext();
        
        experiment1();
        experiment2();
        experiment3();
        
        // Summary
        System.out.println("\n" + "=".repeat(60));
        System.out.println("SCOPE SUMMARY");
        System.out.println("=".repeat(60));
        System.out.println("""
        
        Java Scope Types:
        
        1. Class/Static Scope:
           • Static variables (exist for program lifetime)
           • Accessible from static methods
        
        2. Instance Scope:
           • Non-static variables (tied to object)
           • Accessible via 'this' or object reference
        
        3. Method/Local Scope:
           • Variables declared inside methods
           • Exist only during method execution
           • Stored on stack
        
        4. Block Scope:
           • Variables declared in { } blocks
           • Exist only within that block
        
        5. Parameter Scope:
           • Method parameters
           • Act like local variables
        
        Key Points:
        ✓ Java uses lexical (static) scope
        ✓ Local variables cannot be accessed outside their block
        ✓ Use 'this' to access instance variables when shadowed
        ✓ Variables have different lifetimes (stack vs heap)
        """);
    }
}