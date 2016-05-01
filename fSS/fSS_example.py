from fSS_Algorithms import Plant, fSS

#Example
C, K, dists = 3, 1 / .9, [3, 2, 1]
plants = [Plant(5, 1.5), Plant(6, 3), Plant(7, 1), Plant(2, 3)]
I = fSS(C, K, plants, dists)
I.greedy()