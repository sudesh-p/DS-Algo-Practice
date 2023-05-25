# TC: O(1) Push and Empty , Amortized O(1) for Pop
# SC: O(1) No auxillary DS used
# Did it work on LC : Yes.
# Personal Difficulty while solving it: Still understanding how Pop is Amortized O(1)
class MyQueue:

    def __init__(self):
        self.pushst=[]
        self.popst=[]

    def push(self, x: int) -> None:
        self.pushst.insert(0,x)

    def pop(self) -> int:
        self.peek()
        return self.popst.pop(0)

    def peek(self) -> int:
        if not self.popst:
            while self.pushst:
                self.popst.insert(0, self.pushst.pop(0))
        return self.popst[0]

    def empty(self) -> bool:
        if not self.pushst and not self.popst:
            return True
        return False