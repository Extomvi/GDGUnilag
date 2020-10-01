"""Longest COnsecutive number"""

def longestConsecutive(nums):
    store = set(nums); seen = set()
    res = 0

    for num in nums:
        count = 1
        if num in seen:
            continue
        store.remove(num)
        seen.add(num)

        #checking if it's less than
        current = num - 1
        while current in store:
            count += 1
            store.remove(current)
            seen.add(current)
            current -= 1
        
        #checking if it's greater than
        current = num + 1
        while current in store:
            count += 1
            store.remove(current)
            seen.add(current)
            current += 1

        res = max(count, res)
    return res