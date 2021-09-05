"""
Count unhappy friends
"""


def count_unhappy_friends(n, preferences, pairs):
    d = {}

    for x, y in pairs:
        print(x, y)
        print(preferences[x])
        print(preferences[x].index(y))
        d[x] = set(preferences[x][:preferences[x].index(y)])
        d[y] = set(preferences[y][:preferences[y].index(x)])
        print(d)

    result = 0
    for x in d:
        for y in d[x]:
            if x in d[y]:
                result += 1
                break

    return result


if __name__ == "__main__":
    n = 4
    preferences = [[1,2,3], [3,2,0], [3,1,0], [1,2,0]]
    pairs = [[0,1], [2,3]]

    print(count_unhappy_friends(n, preferences, pairs))
