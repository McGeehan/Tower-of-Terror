import random


class PreShow:
    def play(self):
        print("\n--- THE TWILIGHT ZONE PRE-SHOW ---")
        print("You are about to enter...")
        print("The Hollywood Tower Hotel.")
        print("Tonight's story concerns an elevator.")
        print("---------------------------------\n")


class ElevatorCar:
    def __init__(self, name):
        self.name = name

        # simplified drop profiles
        self.drop_profiles = [
            ["UP", "DROP", "UP", "BIG DROP"],
            ["UP", "BIG DROP", "UP", "DROP", "DROP"],
            ["UP", "DROP", "UP", "DROP", "BIG DROP"],
            ["UP", "UP", "BIG DROP", "DROP"]
        ]

    def run_ride(self):

        profile = random.choice(self.drop_profiles)

        print(f"{self.name} loading passengers...")
        print(f"{self.name} entering elevator shaft...\n")

        for action in profile:
            print(f"{self.name}: {action}")

        print(f"\n{self.name} ride complete!")
        print("-" * 30)


class TowerOfTerror:
    def __init__(self):
        self.preshow = PreShow()

        self.elevators = [
            ElevatorCar("Elevator A"),
            ElevatorCar("Elevator B"),
            ElevatorCar("Elevator C")
        ]

    def start_ride(self):

        self.preshow.play()

        elevator = random.choice(self.elevators)

        print(f"Assigned to: {elevator.name}\n")

        elevator.run_ride()


ride = TowerOfTerror()
ride.start_ride()
