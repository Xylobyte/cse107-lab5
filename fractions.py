import math


def reduce(fraction: tuple):
    """returns the reduced form of a fraction passed into it
    """
    gcd = math.gcd(fraction[0], fraction[1])
    return (int(fraction[0] / gcd), int(fraction[1] / gcd))


def add(fraction1: tuple, fraction2: tuple):
    """returns the sum of two fractions passed into it
    """
    frac1 = (fraction1[0] * fraction2[1], fraction1[1] * fraction2[1])
    frac2 = (fraction2[0] * fraction1[1], fraction2[1] * fraction1[1])
    return reduce((frac1[0] + frac2[0], frac1[1]))


def multiply(fraction1: tuple, fraction2: tuple):
    """returns the product of two fractions passed into it
    """
    return reduce((fraction1[0] * fraction2[0], fraction1[1] * fraction2[1]))


def divide(fraction1: tuple, fraction2: tuple):
    """returns the quotient of two fractions passed into it
    """
    return multiply(fraction1, (fraction2[1], fraction2[0]))


def main():
    """test cases for the functions above
    """
    frac1 = tuple([int(n) for n in input("Enter a fraction >>> ").split("/")])
    frac2 = tuple([int(n) for n in input("Enter a fraction >>> ").split("/")])
    rfrac1 = reduce(frac1)
    rfrac2 = reduce(frac2)
    sum = add(frac1, frac2)
    product = multiply(frac1, frac2)
    quotient = divide(frac1, frac2)

    print("Reduced fractions to {}/{} and {}/{}".format(
        rfrac1[0], rfrac1[1], rfrac2[0], rfrac2[1]))
    print("Sum of the fractions: {}/{}".format(
        sum[0], sum[1]))
    print("Product of the fractions: {}/{}".format(
        product[0], product[1]))
    print("Quotient of the first by the second: {}/{}".format(
        quotient[0], quotient[1]))


if __name__ == "__main__":
    main()
