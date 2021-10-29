class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    def up(self):
        """Makes the elevator go up one floor"""
        pass
    def down(self):
        """Makes the elevator go down one step"""
        pass
    def go_to(self,floor):
        self.current = floor
elevator = Elevator(-1, 10, 0)

elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)

elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current)
