def rob_houses(house_values):
    def rob_line(houses):
        if not houses:
            return 0, []
        if len(houses) == 1:
            return houses[0], [1]

        dp = [(0, []) for _ in range(len(houses) + 1)]
        dp[1] = (houses[0], [1])

        for i in range(2, len(houses) + 1):
            val1, indices1 = dp[i - 1]
            val2, indices2 = dp[i - 2]
            if val1 > val2 + houses[i - 1]:
                dp[i] = (val1, indices1)
            else:
                dp[i] = (val2 + houses[i - 1], indices2 + [i])

        return dp[-1]

    if not house_values:
        return 0, []

    if len(house_values) == 1:
        return house_values[0], [1]

    max1, indices1 = rob_line(house_values[1:])
    max2, indices2 = rob_line(house_values[:-1])

    if max1 > max2:
        return max1, [i + 1 for i in indices1]
    else:
        return max2, indices2

# Example usage
money, houses = rob_houses([100, 300, 400])
print("Maximum money that can be stolen:", money)
print("House positions chosen for attack:", houses)

money, houses = rob_houses([1, 3, 5, 7])
print("Maximum money that can be stolen:", money)
print("House positions chosen for attack:", houses)
