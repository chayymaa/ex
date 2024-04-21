def maxProfit(k, prices):
    n = len(prices)
    if n <= 1:
        return 0

    # Si le nombre de transactions autorisées est supérieur ou égal à la moitié
    # de la longueur du tableau des prix, nous pouvons effectuer des transactions illimitées.
    if k >= n // 2:
        return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))

    # Initialisation du tableau dp
    dp = [[[0] * 2 for _ in range(k+1)] for _ in range(n)]

    for i in range(n):
        for j in range(k, 0, -1):
            if i == 0:
                # Cas de base : le premier jour, nous ne pouvons détenir une action que si nous l'achetons
                dp[i][j][1] = -prices[i]
            else:
                # Mettre à jour les valeurs dp pour ne pas détenir d'actions
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # Mettre à jour les valeurs dp pour détenir une action
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

    return dp[n-1][k][0]

# Exemple d'utilisation :
k1 = 2
prices1 = [2, 4, 1]
print(maxProfit(k1, prices1))  # Sortie: 2

k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
print(maxProfit(k2, prices2))  # Sortie: 7
