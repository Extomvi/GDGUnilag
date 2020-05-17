"""Invalid transactions checker"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        trans, i = [], 0
        for char in transactions:
            trans.append(tuple(char.split(",")))
        trans.sort(key= lambda x: (x[0], x[1]))

        store = set()
        while i < len(trans):
            j = i+1
            while j < len(trans) and trans[j][0] == trans[i][0]:
                if abs(int(trans[i][1]) - int(trans[j][1])) <= 60:
                    if trans[i][3] != trans[j][3]:
                        store.add(",".join(trans[i]))
                        store.add(",".join(trans[j]))

                j += 1
            if int(trans[i][2]) > 1000: store.add(",".join(trans[i]))
            i += 1
        return list(store)
