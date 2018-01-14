def to_base(b):
    def to_base_b(n):
        s = ""
        while n:
            s = str(n % b) + s
            n /= b
        return int(s)
    return to_base_b


def iteration(k, to_dec, to_base, filled_str):
    def iteration_with_constants(n):
        digits = list(filled_str(n)) # make sure the digits list is the correct length
        x_digits = sorted(digits, reverse=True)
        x = int(''.join(x_digits))
        x_dec = to_dec(x)
        y_digits = reversed(x_digits)
        y = int(''.join(y_digits))
        y_dec = to_dec(y)
        z_dec = x_dec - y_dec
        z = to_base(z_dec)
        print '%i: %i(%i) - %i(%i) = %i(%i)' % (n, x_dec, x, y_dec, y, z_dec, z)
        return [x, y, z]
    return iteration_with_constants



class Minion:

    def __init__(self, n, b):
        self.n = n
        self.k = len(str(n))
        self.b = b
        self.cycle = {}
        self.filled_str = lambda x: str(x).zfill(self.k)
        self.iteration = iteration(
            k=self.k,
            to_dec=lambda x: int(str(x), b),
            to_base=to_base(b),
            filled_str=self.filled_str
        )

    def get_iterations(self, z=None):
        if z is None:
            z = self.n

        z_str = self.filled_str(z)
        if z_str not in self.cycle:
            xyz = self.iteration(z)
            new_z = xyz[2]
            if z == new_z:
                """
                answer is 1 because the new z is the same as the last z,
                causing the cycle to get stuck on this value
                """
                return 1
            self.cycle[z_str] = xyz
            return self.get_iterations(new_z)
        else:
            return len(self.cycle)


def answer(n, b):
    minion = Minion(n, b)
    ans = minion.get_iterations()
    # print minion.cycle
    return ans



# print answer(1211, 10)
print answer(210022, 3)
