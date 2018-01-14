from collections import OrderedDict

def to_base_b(b):
    def n_to_base_b(n):
        if n == 0:
            return 0
        digits = []
        while n:
            digits.append(int(n % b))
            n /= b
        return int(''.join(map(str, digits[::-1])))
    return n_to_base_b

def iteration(k, to_dec, to_base, fill_str):
    def iteration_with_constants(n):
        digits = list(fill_str(n)) # make sure the digits list is the correct length
        x_digits = sorted(digits, reverse=True)
        x = int(''.join(x_digits))
        x_dec = to_dec(x)
        y_digits = reversed(x_digits)
        y = int(''.join(y_digits))
        y_dec = to_dec(y)
        z_dec = x_dec - y_dec
        z = to_base(z_dec)
        # print '%i: %i(%i) - %i(%i) = %i(%i)' % (n, x_dec, x, y_dec, y, z_dec, z)
        return [x, y, z]
    return iteration_with_constants



class Minion:

    def __init__(self, n, b):
        self.n = n
        self.k = len(str(n))
        self.b = b
        self.cycle = OrderedDict()
        self.fill_str = lambda x: str(x).zfill(self.k)
        self.iteration = iteration(
            k = self.k,
            to_dec = lambda x: int(str(x), b),
            to_base = to_base_b(b),
            fill_str = self.fill_str
        )

    def get_iterations(self, z=None):
        if z is None: # first iteration
            z = self.n

        z_str = self.fill_str(z)
        if z_str not in self.cycle: # a new z has been encountered, so add it to the hashtable
            xyz = self.iteration(z)
            new_z = xyz[2]
            if z == new_z or z == 0:
                """
                answer is 1 because the new z is the same as the last z,
                causing the cycle to get stuck on this value
                """
                return 1
            self.cycle[z_str] = xyz
            return self.get_iterations(new_z)
        else: # this hash exists already. we're currently at the end of the cycle, so just look for the its starting point
            return len(self.cycle) - self.cycle.keys().index(z_str)


def answer(n, b):
    minion = Minion(n, b)
    return minion.get_iterations()

answer(0, 2)
answer(1211, 10)
answer(210022, 3)
