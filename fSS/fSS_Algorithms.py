class Plant:
    """
    A plant consists of: 1) profit p, 2) temperature constraint b, 3) production
    level t, and 4) outlet temperature out
    """
    def __init__(self, p, b):
        """
        user supplies p and b
        """
        self.p, self.b, self.t, self.out = p, b, 0, 0


class fSS:
    """
    An object of this class represents an instance of the fractional Selective
    Shutdown (fSS) problem; includes greedy algorithm for the problem with
    auxiliary functions
    """
    def __init__(self, C, K, plants, dist, name=''):
        """
        user supplies C, K, plant list, and plant dist. vector (distances between
        contiguous plants)
        """
        self.C, self.K, self.plants, self.N = C, K, plants, len(plants)
        self.e = self.get_effects(dist)
        self.name = name

    def get_effects(self, dist):
        """
        take dist. vector and return dict of effects between all plants
        """
        e = {}
        for i in range(self.N):
            for j in range(i, self.N):
                e[i, j] = self.K**sum(dist[k] for k in range(i, j))
        return e

    def f(self, i, j):
        """
        effective profit of plant i relative to plant j
        """
        return self.plants[i].p * self.e[i, j]

    def Փ(self, i, j):
        """
        the potential of plant i relative to plant j, i.e., how much we can
        raise the temp. at plant i before meeting constraint C at plant j
        """
        return self.e[i, j] * (self.C - self.plants[j].out)

    def sort_on_f(self):
        """
        order plants on f(i, N-1) (effective profit relative to last plant)
        """
        fs = [(self.f(i, self.N-1), i) for i in range(self.N)]
        fs.sort(reverse=1)
        return [p[1] for p in fs]

    def greedy(self):
        """
        solve instance optimally with greedy algorithm
        """
        live = self.sort_on_f()
        while live:
            i = live.pop(0)
            plant = self.plants[i]

            # highest temp. increase at plant i (first to meet a constraint)
            plant.t = min(plant.b, min(self.Փ(i, j) for j in range(i, self.N)))

            for j in range(i, self.N):
                if j in live[1:] and plant.t == self.Փ(i, j): live.remove(j)
                self.plants[j].out += plant.t / self.e[i, j]

        self._print_solution()

    def _print_solution(self):
        """
        print optimal solution after running greedy
        """
        print('~~%s~~' % self.name)
        print('temps: ' + ', '.join('%.2f' % r.t for r in self.plants))
        profits = [r.t * r.p for r in self.plants]
        print('power: ' + ', '.join('%.2f' % p for p in profits))
        print('total: %.2f\n' % sum(profits))


