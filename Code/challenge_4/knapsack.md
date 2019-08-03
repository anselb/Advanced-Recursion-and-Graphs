# Knapsack Problem

## 5 Steps of Dynamic Programming applied to Knapsack Problem
- Identify the subproblems - Whether or not an item can be put into the knapsack
- Guess the first choice - Add a random item into the knapsack
- Recursively define the value of an optimal solution - Take the maximum value of the recursive branches of a solution
- Compute the value of an optimal solution (recurse and memoize) - The recursion goes through all the combinations of items that can be added to the knapsack. If the weight for the current set of items has already been calculated, return it.
- Solve original problem by reconstructing the sub-problems - The values for possible options are calculated when the base case is reached (weight is maxed out). The max of the value added is taken at each recursive branch, so the most value that could be added is reached at the end.
