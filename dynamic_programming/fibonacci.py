
def fibonacci_iter(n):
    results = [0,1]
    i = 2
    while i <= n:
        results.append(results[i-1] + results[i-2])
        i += 1
    return results[-1]


def fibonacci_rec(n):
    if n < 2:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)


"""Dynamic programmimg is recursion with memonization
can ignore memonized recursion its kind of linear time O(1) * n (subproblems)
    time = no of subproblems / time per subproblem
Returns:
    [type] -- [description]
"""
memo = {}
def fibonacci_dp(n):
    if n in memo:
        return memo[n]

    if n <= 2:
        f = 1
    else:
        f = fibonacci_dp(n-1) + fibonacci_dp(n-2)
        memo[n] = f
    return f


"""same computation as the memonization
topological sort of the sub-problem dependency dag
to compute f(n), need to know f(n-1) and f(n-2) which inturn depends on
can make it constant space by only storing the last two items
Returns:
    [type] -- [description]
"""
sack = {}
def fibonacci_bottom_up(n):
    for i in range(n+1):
        if i <= 2:
            f = 1
        else:
            f = sack[i-1] + sack[i-2]
        sack[i] = f
    return sack[n]

n = 10
print(fibonacci_iter(n))
print(fibonacci_rec(n))
print(fibonacci_dp(n))
print(fibonacci_bottom_up(n))


"""Five easy steps to Dynamic Programming
1. define subproblems
2. guess (part of solution)
3. relate subproblem solutions
4. build an algorithm - recurse & memonize
    bottom-up approach (building a dp table)
5. solve the original problem
"""
