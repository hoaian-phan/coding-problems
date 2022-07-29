class PhoneDirectory:
    from collections import deque

    def __init__(self, maxNumbers: int):
        self.available = deque()
        for i in range(maxNumbers):
            self.available.append(i)
        
        

    def get(self) -> int:
        return self.available.popleft() if self.available else -1
        

    def check(self, number: int) -> bool:
        print(self.available)
        return True if number in self.available else False


    def release(self, number: int) -> None:
        if number not in self.available:
            self.available.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)