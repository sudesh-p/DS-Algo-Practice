class BrowserHistory:

    def __init__(self, homepage: str):
        self.history=[homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        self.curr += 1
        while self.curr<len(self.history):
            self.history.pop()
        self.history.append(url)

    def back(self, steps: int) -> str:
        if steps > self.curr:
            self.curr = 0
        else:
            self.curr -= steps
        return self.history[self.curr]
            
    def forward(self, steps: int) -> str:
        if steps+self.curr >= len(self.history):
            self.curr = len(self.history)-1
        else:
            self.curr += steps
        return self.history[self.curr]