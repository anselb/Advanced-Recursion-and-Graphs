# Knapsack Problem

## 5 Steps of Dynamic Programming applied to Knapsack Problem
- Identify the subproblems - Maximizing n-1 items with and without the current item
- Guess the first choice - Add a random item into the knapsack
- Recursively define the value of an optimal solution - Max between when the item is in vs when the item is out
- Compute the value of an optimal solution (recurse and memoize) - The recursion goes through all the combinations of items that can be added to the knapsack. If the weight for the current set of items has already been calculated, return it.
- Solve original problem by reconstructing the sub-problems - The values for possible options are calculated when the base case is reached (weight is maxed out). The max of the value added is taken at each recursive branch, so the most value that could be added is reached at the end.

## Resources
- Used [this side](https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html) for test cases.
- Looked at [these slides](https://docs.google.com/presentation/d/1QoK6PMX0eiJ6XEQsKa5ZkU-_EJHZ-uG1Pc6attOBkAQ/) for second solution.
