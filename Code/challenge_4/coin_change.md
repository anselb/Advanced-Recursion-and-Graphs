# Coin Change Problem
The one to figure out all the ways to create change given a set of coins and the total change needed

## 5 Steps of Dynamic Programming applied to Knapsack Problem
- Identify the subproblems - Count the ways to combine the coins with a coin in the set and without the coin in the set
- Guess the first choice - Continually remove a coin randomly
- Recursively define the value of an optimal solution - Calculate the number of the coin combinations when the coin is in the set and when it is out
- Compute the value of an optimal solution (recurse and memoize) - The recursive function calls handle the variations of the different coin combinations, and the base cases tell the function when to stop making recursive calls
- Solve original problem by reconstructing the sub-problems - When the counts are calculated for each possibility of a coin in and out of the coin set, add up all the counts.

## Resources
- https://www.geeksforgeeks.org/coin-change-dp-7/
