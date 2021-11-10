# Fibonacci Series with Memoization

def fibMemo(n, memo):
    
    if n==1:
        return 0

    if n==2:
        return 1

    if not n in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
        # print(memo)
            
    return memo[n]


myDict = {}         #Empty dict
print(fibMemo(5, myDict))