"""
Given a set of coins values coins = {c1, c2,.., ck} and a target sum of money m, what's the minimum number of coins that form the sum m?
"""

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


memo = {}
def min_coins(target, coins):
    if target in memo:
        return memo[target]
    
    if target == 0:
        result = 0
    
    result = None
    for coin in coins:
        sub_problem = target - coin
        if sub_problem < 0:
            continue
        result =  min_ignore_none(result, min_coins(sub_problem, coins) + 1)

    memo[target] = result
    return result

## O(target * k (no. of coins))

## Bottom up approach

def min_coinb_bu(target, coins):
    memo = {}

    memo[0] = 0
    for i in range(1, target +_1):
        for coin in coins:
            sub_target = i - coin
            if sub_target < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(sub_target) + 1)
    
    return memo[target]
        