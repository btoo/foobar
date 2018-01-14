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
        self.iteration_count = 0

    def get_iterations(self, z=None):
        if z is None:
            z = self.n

        z_str = str(z).zfill(self.k)
        if z_str not in self.cycle:
            xyz = self.iteration(z)
            new_z = xyz[2]
            if z == new_z:
                # print "answer is 1 because the new z is the same as the last z, causing the cycle to get stuck on this value"
                # print xyz
                return 1
            self.cycle[z_str] = xyz
            self.iteration_count += 1
            return self.get_iterations(new_z)
        else:
            # print 'last', z_str
            return self.iteration_count


def answer(n, b):
    minion = Minion(n, b)
    return minion.get_iterations()



answer(1211, 10)