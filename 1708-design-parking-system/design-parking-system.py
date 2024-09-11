class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.map = defaultdict(int)
        self.map[1] = big
        self.map[2] = medium
        self.map[3] = small
        

    def addCar(self, carType: int) -> bool:
        if self.map[carType] < 1:
            return False
        self.map[carType] -= 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)