"""
Mahesh Goldberg is a traveling salesman. He works in N towns. Each day he sells his products in one of the towns. The towns that are chosen on any two successive days should be different, and a town i can be chosen at most c of i times. Write an algorithm to determine the number of days when he can sell in the given towns, following the above-mentioned rules.

For example, a salesman visits three towns. The first, second, and third towns are chosen seven times, two times, and three times respectively. The different towns are selected on successive days in a sequence. First, second, first, third, first, second, first, third, first, third, and first. So the maximum number of days during which a salesman can sell is 11.

Input: [7, 2, 3]
Output: 11
"""

def max_sales_day_recursive(towns, prev_town=-1, total_days=0):
    # sort town by remaining visits in descending order
    towns.sort(key=lambda x: x[1], reverse=True)

    # find the next town to visit
    for i in range(len(towns)):
        if towns[i][1] > 0 and towns[i][0] != prev_town:
             next_towns = towns[:]
             next_towns[i] = (towns[i][0], towns[i][1] -  1)
             return max_sales_day_recursive(next_towns, towns[i][0], total_days + 1)
    return total_days


def max_sales_days(towns_visits):
    towns = [(i, visits) for i, visits in enumerate(towns_visits)]
    return max_sales_day_recursive(towns)