from fSS.fSS_Algorithms import Plant, fSS

# Example 1
C, K, dists = 3, 1 / .9, [3, 2, 1]
plants = [Plant(5, 1.5), Plant(6, 3), Plant(7, 3), Plant(2, 3)]
I = fSS(C, K, plants, dists, 'Example 1')
I.greedy()

# Example 2
C, K, dists = 3, 1 / .9, [3, 3, 4, 1]
plants = [Plant(4, 3), Plant(5, 3), Plant(6, 2), Plant(7, 3), Plant(2, 3)]
I = fSS(C, K, plants, dists, 'Example 2')
I.greedy()