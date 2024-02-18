class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def degree(self):
        return len(self.coeffs) - 1

    def add(self, other):
        if self.degree() >= other.degree():
            result_coeffs = self.coeffs.copy()
            for i in range(other.degree() + 1):
                result_coeffs[i] += other.coeffs[i]
        else:
            result_coeffs = other.coeffs.copy()
            for i in range(self.degree() + 1):
                result_coeffs[i] += self.coeffs[i]
        return Polynomial(result_coeffs)

    def multiply(self, other):
        result_degree = self.degree() + other.degree()
        result_coeffs = [0] * (result_degree + 1)

        for i in range(self.degree() + 1):
            for j in range(other.degree() + 1):
                result_coeffs[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result_coeffs)

    def __str__(self):
        terms = []

        for i, coeff in enumerate(self.coeffs[::-1]):
            if coeff != 0:
                term_str = f"{coeff}x^{self.degree() - i}" if self.degree() - i > 1 else f"{coeff}x"
                terms.append(term_str)

        return " + ".join(terms[::-1]) if terms else "0"


def main():
    print("Enter the coefficients of the first polynomial, separated by spaces (highest degree first):")
    coeffs1 = [int(coeff) for coeff in input().split()]

    print("Enter the coefficients of the second polynomial, separated by spaces (highest degree first):")
    coeffs2 = [int(coeff) for coeff in input().split()]

    polynomial1 = Polynomial(coeffs1)
    polynomial2 = Polynomial(coeffs2)

    # Perform operations
    sum_result = polynomial1.add(polynomial2)
    product_result = polynomial1.multiply(polynomial2)

    # Output results
    print("First polynomial:", polynomial1)
    print("Second polynomial:", polynomial2)
    print("Sum:", sum_result)
    print("Product:", product_result)


if __name__ == "__main__":
    main()
