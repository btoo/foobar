def iteration(k):
    def iteration_with_k(n):
        digits = list(str(n).zfill(k)) # make sure the digits list is the correct length
        x_digits = sorted(digits, reverse=True)
        x = int(''.join(x_digits))
        y_digits = reversed(x_digits)
        y = int(''.join(y_digits))
        z = x - y
        return [x, y, z]
    return iteration_with_k



class Minion:

    def __init__(self, n, b):
        self.cycle = {}
        self.n = n
        self.k = len(str(n))
        self.iteration = iteration(self.k)
        self.b = b

    def get_iterations(self, z=None):
        if z is None:
            z = self.n

        if str(z).zfill(self.k) not in self.cycle:
            xyz = self.iteration(z)
            self.cycle[str(z).zfill(self.k)] = xyz
            self.get_iterations(xyz[2])




minion = Minion(1211, 10)
# minion = Minion(999, 10)
# print(minion.k)
minion.get_iterations()
print(minion.cycle)
