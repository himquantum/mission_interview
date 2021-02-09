import permutation


def answer(coins, amount):
    total = 0
    for i in range(0, len(coins)):
        total += amount // coins[i]
        if amount >= coins[i]:
            amount = amount % coins[i]
            #print(f'i: {i}, coin selected: {coins[i]}, total coins: {total} , remaining amount: {amount}')
        if amount == 0:
            return total
    return -1


array = [8, 5, 3]
amount = 18
coin_lists = permutation.permutation(array)
outputs = []
for coins in coin_lists:
    outputs.append(answer(coins, amount))

print(outputs)
