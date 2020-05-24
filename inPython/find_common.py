def find_common(s1, s2):
    store, count = {}, 0
    for i in s1:
        if i in store: store[i]+=1
        else: store[i] = 1
    for i in s2:
        if i in store:
            if store[i] > 0:
                store[i] -=1
                count+=1
        else: pass
    return count
