class MakingChange:
    def minimumCoins(self, money, coins):
        min_coins = [money+1] * (money + 1)

        min_coins[0] = 0
        
        for coin in coins:
            for i in range(coin, money + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
        if min_coins[money] != money+1:
        	return min_coins[money]
        else: 
        	return -1 

