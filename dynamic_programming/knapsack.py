
"""
tabulation approach (bottom up)
"""
def knapsack(weights, values, capacity):
    combinations = [[0] * (capacity + 1)] * (len(weights) + 1)

    for i in range(len(combinations)):
        for j in range(len(combinations[i])):
            if i == 0 or j == 0:
                combinations[i][j] = 0
            elif weights[i-1] > j:
                combinations[i][j] = combinations[i-1][j]
            else:
                combinations[i][j] = max(combinations[i-1][j], combinations[i-1][j - weights[i-1]] + values[i-1])
    return combinations[i][capacity]

if __name__ == "__main__":
    print(knapsack([1,2,3,4], [1,3,4,6], 6))
