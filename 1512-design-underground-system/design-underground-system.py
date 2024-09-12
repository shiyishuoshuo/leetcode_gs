class UndergroundSystem:

    def __init__(self):
        self.idToCheckIn = defaultdict(tuple)
        self.stationToTime = defaultdict(tuple)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idToCheckIn[id] = (stationName, t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id not in self.idToCheckIn:
            return
        startStation, start_time = self.idToCheckIn[id]
        if (startStation, stationName) not in self.stationToTime:
            self.stationToTime[(startStation, stationName)] = (0, 0)
        total_time, total_count = self.stationToTime[(startStation, stationName)]
        total_time += (t - start_time)
        total_count += 1
        self.stationToTime[(startStation, stationName)] = (total_time, total_count)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not in self.stationToTime:
            return -1
        total_time, total_count = self.stationToTime[(startStation, endStation)]
        return total_time / total_count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)