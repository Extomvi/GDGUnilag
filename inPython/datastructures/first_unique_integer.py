"""First Unique Integer"""

'''
You have a queue of integers, you need to retrieve the first unique integer in the queue
'''

class FirstUniqueCharacter:
    def __init__(self, nums: list[int]):  #Not sure why this throws an error though(LOL)
        self.store = {}
        self.check = set()
        self.nums = nums
        
        for i in nums:
            if i in self.store:
                self.store[i] += 1
                if i in self.check:
                    self.check.remove(i)
            else:
                self.store[i] = 1
                self.check.add(i)
    
    def showFirstUnique(self) -> int:
        if not self.check:
            return -1
        for i in self.nums:
            if i in self.check:
                return i
        
    def add(self, value: int) -> None:
        self.nums.append(value)
        if value in self.store:
            self.store[value] += 1
            if value in self.check:
                self.check.remove(value)
        else:
            self.store[value] = 1
            self.check.add(value)