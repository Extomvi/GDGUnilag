from collections import Counter

def counting(arr):
    store = dict(Counter(arr[0]))
    result = []

    for i in range(1, len(arr)):
        temp = Counter(arr[1])
        remove = []
        for chars in store:
            if chars not in temp:
                remove.append(chars)
            else:
                store(chars) = min(store[chars], temp[chars])

        for chars in remove:
            del(store[chars])

    for i in store:
        value = store[i]
        while value > 0:
            result.append(i)
            value -= 1
    return result 