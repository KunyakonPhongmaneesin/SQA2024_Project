class Car:
    def drive(self) -> str:
        return "Car is driving on the road"

class Boat:
    def sail(self) -> str:
        return "Boat is sailing on the water"

# Adapter for Boat to adapt it to the Car interface
class BoatAdapter(Car):
    def __init__(self, boat: Boat):
        self.boat = boat

    def drive(self) -> str:
        # Adapting the sail method to work as the drive method
        return self.boat.sail()

# Usage Example
def main():
    car = Car()
    boat = Boat()
    boat_adapter = BoatAdapter(boat)

    # Both can now use the 'drive' method
    print(car.drive())
    print(boat_adapter.drive())

if __name__ == "__main__":
    main()
