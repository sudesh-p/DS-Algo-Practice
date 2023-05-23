class MinStack:

    def __init__(self):
        self.arr= []
        self.currMin = pow(2,31)
        self.prevMin = []
        

    def push(self, val: int) -> None:
        if val<=self.currMin:
            self.prevMin.append(self.currMin)
            self.currMin = val
        self.arr.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.currMin:
            self.currMin = self.prevMin.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.currMin