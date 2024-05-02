def is_subsequence(s: str, t: str) -> bool:
    # elimina pass e inserisci il tuo codice
    listS:list = []
    listT:list = []
    for i in s:
        listS.append(i)
    for i in t:
        listT.append(i)
    for i in listS:
        if i in listT:
            return True
        else:
            break
print(is_subsequence("abc","ariboc"))



def third_max(nums: list[int]) -> int:
    # elimina il pass e inserisci il tuo codice
    # potete utilizzare queste tre variabili di comodo
    first_max = second_max = third_max = float('-inf')
    numsClear:list = []
    for i in nums:
        if i not in numsClear:
            numsClear.append(i)
    numsClear.sort()
    numsClear.reverse()
    
            
    third_max: float = numsClear[-1]
    return third_max
