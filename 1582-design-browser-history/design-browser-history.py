class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_stack = []
        self.back_stack = []
        self.visit(homepage)
        

    def visit(self, url: str) -> None:
        self.back_stack.append(url)
        self.forward_stack.clear()
        

    def back(self, steps: int) -> str:
        while len(self.back_stack) > 1 and steps > 0:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
        return self.back_stack[-1]
        
        

    def forward(self, steps: int) -> str:
        while len(self.forward_stack) and steps > 0:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1        
        return self.back_stack[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)