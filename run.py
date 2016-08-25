from permute.finder import factorial_finder, PermutationFinder


def main():
    num_digits = int(input('Give an integer number of digits between 1 and 9: '))
    factorials = factorial_finder(num_digits)
    n = int(input('Provide a number between 1 and {0}: '.format(factorials[-1])))

    print 'Calculating the {0}th permutation of {1} digits'.format(n, num_digits)

    finder = PermutationFinder(num_digits, n, factorials)
    permutation = finder.find_permutation()

    print 'The {0}th permutation is: {1}'.format(n, permutation)


if __name__ == '__main__':
    main()
