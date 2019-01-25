from byotest import *

#dictionary of coins (20 of each denomination og coins)
usd_coins = {
    100:20,
    50:20,
    25:20,
    10:20,
    5:20,
    1:20
    }
    
eur_coins = {
    100:20,
    50:20,
    20:20,
    10:20,
    5:20,
    2:20,
    1:20
    }

def get_change(amount, coins=eur_coins):
   
    change = []
    for denomination in sorted(coins.keys(),reverse=True):
        while denomination <= amount and coins[denomination] >0:
            amount -= denomination
            coins[denomination] -=1
            change.append(denomination)
    
    #error message if insuffient coins to give coins        
    if amount !=0:
        raise Exception ("Sorry, there is insuffient coins to give change")
            
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(9), [5, 2, 2])
test_are_equal(get_change(35, usd_coins), [25, 10])
test_are_equal(get_change(9, {5:1, 2:1, 1:2}), [5, 2, 1, 1])

print("All tests pass!!")