"""
Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.
"""

def distribute_candies(candies):
    unique_candies = len(set(candies))
    return min(unique_candies, len(candies)//2)

    candies.sort()
    unique_candies = 1
    
    for i in range(1, len(candies)):
        if candies[i] != candies[i-1]:
            unique_candies += 1

        if unique_candies == len(candies) // 2:
            break

    return min(unique_candies, len(candies)//2)
