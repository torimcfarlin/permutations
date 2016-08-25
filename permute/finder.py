from math import floor


class PermutationFinder(object):
    def __init__(self, num_digits, n, factorials):
        self.num_digits = num_digits
        self.digits = list(range(1, self.num_digits + 1))
        self.remainder = self.n = n

        factorials.reverse()
        self.factorials = factorials
        self.is_max = self._check_for_max_permutation()

    def _check_for_max_permutation(self):
        if self.n == self.factorials[0]:
            return True
        else:
            return False

    def _get_next_index(self, factorial):
        return int(floor(self.remainder / factorial))

    def _set_remainder(self, index, factorial):
        self.remainder -= index * factorial

    def find_permutation(self):

        if self.is_max:
            permutation = self.digits
            permutation.reverse()
            return permutation

        permutation = []

        for factorial in self.factorials[1:]:
            k = self._get_next_index(factorial)
            self._set_remainder(k, factorial)
            digit = self.digits.pop(k)
            permutation.append(digit)

        permutation.append(self.digits.pop())

        return permutation


def factorial_finder(num_digits):
    factorials = []
    f = 1
    for n in range(1, num_digits + 1):
        f *= n
        factorials.append(f)

    return factorials
