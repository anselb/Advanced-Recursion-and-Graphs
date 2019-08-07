# First solution take from https://www.geeksforgeeks.org/coin-change-dp-7/


# Returns the count of ways we can sum coins[0...num_coins-1] coins to get sum
def count(coins, num_coins, sum):
    # If sum is 0 then there is 1 solution (do not include any coin)
    if (sum == 0):
        return 1

    # If sum is less than 0 then no solution exists
    if (sum < 0):
        return 0

    # If there are no coins and sum is greater than 0, then no solution exists
    if (num_coins <= 0 and sum >= 1):
        return 0

    # count is sum of solutions (i)
    x = count(coins, num_coins - 1, sum)
    # including coins[num_coins-1] (ii) excluding coins[num_coins-1]
    y = count(coins, num_coins, sum - coins[num_coins - 1])
    return x + y


# Driver program to test above function
# arr = [1, 2, 3]
# arr = [2, 5, 3, 6]
# num_coins = len(arr)
# 4
# print(count(arr, num_coins, 4))
# for i in range(11):
#     print(i, count(arr, num_coins, i))


# Iterative solution
def other_count(coins, num_coins, sum):
    combo_arr = [0 for i in range(sum + 1)]

    for sum_ind in range(1, sum + 1):
        for coin in coins:
            if coin == sum_ind:
                combo_arr[sum_ind] += 1
            if sum_ind - coin >= 1:
                combo_arr[sum_ind] += combo_arr[sum_ind - coin]

    return combo_arr[sum]


def main():
    arr = [2, 5, 3, 6]
    num_coins = len(arr)
    # 5
    print("For the input:")
    print(f"coins - {arr}, number of coins - {num_coins}, and coin sum - {10}")
    print("The optimal result is:")
    print(f"A total of {5} different combinations")
    print("The function returned:")
    result = count(arr, num_coins, 10)
    print(f"A total of {result} different combinations")


if __name__ == '__main__':
    main()
