# Coin Change Problem  in Python

#Finf the min number of coins required to accomplise 
def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins)-1   #Get the max coin value index
    result = []
    
    while True:
        
        coinValue = coins[index]  #Get coin vlaue
        
        #Total number greater than Current max coin value (Subtract operation)
        if N >= coinValue:
            N = N - coinValue
            result.append(coinValue)
            
        # Total number less than current max value (Moved to immidiate next max value in the coin list)
        if N < coinValue:
            index -= 1
        
        # Total number equal to zero (Stop looping process)
        if N == 0:
            break
        
    return result

coins = [1,2,5,20,50,100]
numbers = coinChange(201, coins)
print(numbers)
print("Coin Numbers", len(numbers))