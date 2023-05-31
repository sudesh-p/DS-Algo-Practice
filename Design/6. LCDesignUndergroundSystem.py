# TC: O(1) - All are Constant Time Operations.
# SC: O(N+M) No.of Passengers + No. of Unique Routes (Combinations of StartStations, EndStations)
# Did it work on LC : Yes.
# Personal Difficulty while solving it: None

class UndergroundSystem:
    def __init__(self):
        self.checker = {}
        self.routeTotalTime = defaultdict(int)
        self.routeCount = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checker[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        passenger = self.checker.pop(id)
        route = (passenger[0], stationName)
        
        self.routeTotalTime[route] += (t-passenger[1])
        self.routeCount[route] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routeTotalTime[route]/self.routeCount[route]