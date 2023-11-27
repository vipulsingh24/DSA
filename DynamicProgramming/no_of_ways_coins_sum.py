
def no_of_ways(target, coins):
    memo = {}
    memo[0] = 1

    for i in range(1, target + 1):
        memo[i] = 0

        for coin in coins:
            sub_target = i - coin
            if sub_target < 0 :
                continue

            memo[i] = memo[i] + memo[sub_target]

    return memo[target]

"""
no_of_ways(5, [1,2, 4])
-> memo [ {0: 1}]

for:
   memo = {0: 1, 1: 1, 2: 2}
"""