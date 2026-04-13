#!/usr/bin/env python3
"""
Ride-Hailing Pricing Engine - OOP Version
Demonstrates Object-Oriented Programming with encapsulation
APT1030-A Fundamentals of Programming Languages
"""

class RideHailing:
    """Class representing a ride-hailing service"""
    
    # Class constants
    BASE_FARE = 200.0  # KES
    COST_PER_KM = 50.0  # KES per km
    
    def __init__(self, distance, surge_multiplier=1.0):
        """Constructor - initialize ride details"""
        self._distance = distance  # Protected attribute
        self._surge_multiplier = surge_multiplier
        self._fare = None
    
    # Properties (getters and setters)
    @property
    def distance(self):
        return self._distance
    
    @distance.setter
    def distance(self, value):
        if value < 0:
            raise ValueError("Distance cannot be negative")
        self._distance = value
        self._fare = None  # Reset fare when distance changes
    
    @property
    def surge_multiplier(self):
        return self._surge_multiplier
    
    @surge_multiplier.setter
    def surge_multiplier(self, value):
        if value < 1.0:
            raise ValueError("Surge multiplier must be at least 1.0")
        self._surge_multiplier = value
        self._fare = None
    
    def calculate_base_fare(self):
        """Calculate fare without surge pricing"""
        return self.BASE_FARE + (self._distance * self.COST_PER_KM)
    
    def calculate_fare(self):
        """Calculate final fare with surge if applicable"""
        if self._fare is None:
            base = self.calculate_base_fare()
            self._fare = base * self._surge_multiplier
        return self._fare
    
    def display_fare(self):
        """Display fare details"""
        fare = self.calculate_fare()
        base_fare = self.calculate_base_fare()
        
        print("\n" + "="*50)
        print("   RIDE DETAILS (OOP VERSION)")
        print("="*50)
        print(f"Distance: {self._distance} km")
        print(f"Base Fare: KES {self.BASE_FARE:,.2f}")
        print(f"Rate per km: KES {self.COST_PER_KM:,.2f}")
        
        if self._surge_multiplier != 1.0:
            print(f"Surge Multiplier: {self._surge_multiplier}x")
            print(f"Original Fare: KES {base_fare:,.2f}")
        
        print("-" * 50)
        print(f"💰 TOTAL FARE: KES {fare:,.2f}")
        print("="*50)


class SurgeRide(RideHailing):
    """Inheritance example - Special ride type with surge pricing"""
    
    def __init__(self, distance, surge_multiplier=1.5):
        super().__init__(distance, surge_multiplier)
        print("⚠️  Surge pricing is active!")


def main():
    """Main program - OOP approach"""
    print("="*50)
    print("   NAIROBI RIDE-HAILING PRICING (OOP)")
    print("="*50)
    print(f"\nBase Fare: KES {RideHailing.BASE_FARE}")
    print(f"Cost per km: KES {RideHailing.COST_PER_KM}")
    
    # Get input
    distance = float(input("\nEnter distance (km): "))
    surge_input = input("Is surge pricing active? (y/n): ").lower()
    
    if surge_input == 'y':
        multiplier = float(input("Enter surge multiplier (e.g., 1.5): "))
        ride = SurgeRide(distance, multiplier)
    else:
        ride = RideHailing(distance)
    
    # Display fare
    ride.display_fare()
    
    # Demonstrate OOP features
    print("\n--- OOP Characteristics ---")
    print("✓ Encapsulation (data hidden in object)")
    print("✓ Inheritance (SurgeRide extends RideHailing)")
    print("✓ Methods operate on object data")
    print("✓ Reusable and extensible")


if __name__ == "__main__":
    main()