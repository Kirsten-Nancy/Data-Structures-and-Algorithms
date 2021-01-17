prices = [7, 1, 5, 3, 6, 4]
def brute_force():
    maximum_profit = 0
    for k in range(len(prices)):
        for j in range(k + 1, len(prices)):
            current_profit = prices[j] - prices[k]
            if current_profit > maximum_profit:
                maximum_profit = current_profit
            #     Showing the pairs
            print(prices[k], prices[j])
    return maximum_profit


print(brute_force())

# Optimized O(n)
def best_stock():
    # Empty array
    if not prices:
        return 0
    minimum_price = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < minimum_price:
            minimum_price = prices[i]
        elif prices[i] - minimum_price > max_profit:
            max_profit = prices[i] - minimum_price
        # simplification of the above
        # else:
        #     # That current price of stock is greater that buying price
        #     current_profit = prices[i] - minimum_price
        #     if current_profit > max_profit:
        #         max_profit = current_profit
    return max_profit


print(best_stock())



# Third approach of finding the least element and start from the next index to find max
# least = min(prices)
# index_of_least = prices.index(least)
# for i in range(index_of_least + 1, len(prices)):
#     current_profit = prices[i] - least
#     if current_profit > max_profit:
#         max_profit = current_profit
# print(max_profit)
