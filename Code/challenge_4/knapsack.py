import time


def knapsack(sack_cap, obj_weights, obj_profits, curr_sack=None, sacks=None, cache=None):
    if sacks is None:
        sacks = []

    if curr_sack is None:
        item_ind = 0
    else:
        item_ind = len(curr_sack)

    if curr_sack is None:
        curr_sack = []

    # if cache is None:
    #     cache = {}
    # if str(curr_sack) in cache:
    #     current_weight = cache[str(curr_sack)][0]
    #     current_profit = cache[str(curr_sack)][1]
    # else:
    current_weight = 0
    current_profit = 0
    for sack_ind in range(len(curr_sack)):
        if curr_sack[sack_ind] == 1:
            current_weight += obj_weights[sack_ind]
            current_profit += obj_profits[sack_ind]
        # cache[str(curr_sack)] = (current_weight, current_profit)

    skip_sack = curr_sack[:]
    if len(curr_sack) == len(obj_weights):
        return (current_profit, curr_sack)
    elif current_weight + obj_weights[item_ind] <= sack_cap:
        keep_sack = curr_sack[:]
        keep_sack.append(1)
        keep_item_sack = knapsack(sack_cap, obj_weights, obj_profits,
                                  keep_sack, sacks, cache)
        sacks.append(keep_item_sack)

    skip_sack.append(0)
    skip_item_sack = knapsack(sack_cap, obj_weights, obj_profits,
                              skip_sack, sacks, cache)
    sacks.append(skip_item_sack)

    return max(sacks)


# Taken from CS 2.2 Dynamic Programming slides
def other_knapsack(items, capacity):
    if len(items) == 0 or capacity == 0:
        return 0

    item = items.pop()
    item_cap = item[0]
    item_val = item[1]

    if item_cap > capacity:
        return other_knapsack(items, capacity)

    value_without = other_knapsack(items[:], capacity)
    value_with = other_knapsack(items[:], capacity - item_cap) + item_val

    return max(value_without, value_with)


def main():
    # sack_capacity = 26
    # object_weights = [12, 7, 11, 8, 9]
    # object_profits = [24, 13, 23, 15, 16]
    #
    # optimal_items = [0, 1, 1, 1, 0]

    sack_capacity = 165
    object_weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    object_profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]

    optimal_items = [1, 1, 1, 1, 0, 1, 0, 0, 0, 0]

    # sack_capacity = 6404180
    # object_weights = [382745, 799601, 909247, 729069, 467902, 44328, 34610,
    #                   698150, 823460, 903959, 853665, 551830, 610856, 670702,
    #                   488960, 951111, 323046, 446298, 931161, 31385, 496951,
    #                   264724, 224916, 169684]
    # object_profits = [825594, 1677009, 1676628, 1523970, 943972, 97426, 69666,
    #                   1296457, 1679693, 1902996, 1844992, 1049289, 1252836,
    #                   1319836, 953277, 2067538, 675367, 853655, 1826027, 65731,
    #                   901489, 577243, 466257, 369261]
    #
    # optimal_items = [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
    #                  1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1]

    optimal_indices = []
    optimal_value = 0
    for item_ind in range(len(optimal_items)):
        if optimal_items[item_ind] == 1:
            optimal_indices.append(item_ind)
            optimal_value += object_profits[item_ind]

    start = time.time()
    result = knapsack(sack_capacity, object_weights, object_profits)
    finish = time.time()
    result_weight = result[0]
    result_sack = result[1]
    result_indices = []
    for sack_ind in range(len(result_sack)):
        if result_sack[sack_ind] == 1:
            result_indices.append(sack_ind)

    print("For this input:")
    print(f"Object weights: {object_weights}")
    print(f"Object values: {object_profits}")
    print(f"Capacity of knapsack: {sack_capacity}")
    print("\n")
    print(f"Optimal weight: {optimal_value}, got: {result_weight}")
    print(f"Optimal items: {optimal_indices}, got: {result_indices}")
    print(f"Matches?: {optimal_indices == result_indices}")
    print(f"Finished in {finish - start} seconds")

    # item_tuples = []
    # for item_ind in range(len(object_weights)):
    #     tup = (object_weights[item_ind], object_profits[item_ind])
    #     item_tuples.append(tup)
    #
    # start = time.time()
    # result = other_knapsack(item_tuples, sack_capacity)
    # finish = time.time()
    # result_weight = result
    #
    # print(f"Optimal weight: {optimal_value}, got: {result_weight}")
    # print(f"Matches?: {optimal_value == result_weight}")
    # print(f"Finished in {finish - start} seconds")


if __name__ == '__main__':
    main()
