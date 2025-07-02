def karatsuba_multiplication(num1, num2, i):
    if num1 < 10 and num2 < 10:
        return num1 * num2  # Base case: fall back to traditional multiplication

    # Calculate the size of the numbers
    n = max(len(str(num1)), len(str(num2)))
    n2 = n // 2

    # Split the digit sequences in the middle
    a, b = divmod(num1, 10**n2)
    c, d = divmod(num2, 10**n2)
    print("\n" + " " * i * 4 + "There is: " + "a =", a, ", b =", b, ", c =", c, ", d =", d)

    # 3 recursive calls made to numbers approximately half the size
    print(" " * i * 4 + "Calculating z1" + "'" * i + "=", a, "*", c, end="")
    z1 = karatsuba_multiplication(a, c, i+1)
    if a < 10 and c < 10:
        print(" =", z1)
    else:
        print(" " * i * 4 + "So, z1" + "'" * i + " =", z1)
    print(" " * i * 4 + "Calculating z2"  + "'" * i + "=", b, "*", d, end="")
    z2 = karatsuba_multiplication(b, d, i+1)
    if b < 10 and c < 10:
        print(" =", z2)
    else:
        print(" " * i * 4 + "So, z2" + "'" * i + " =", z2)
    print(" " * i * 4 + "Calculating z3" + "'" * i + "= (" + str(a) + " + " + str(b) + ") * (" + str(c) + " + " + str(d) + ")", end="")
    z3 = karatsuba_multiplication((a + b), (c + d), i+1)
    if a + b < 10 and c + d < 10:
        print(" =", z3)
    else:
        print(" " * i * 4 + "So, z3" + "'" * i + " =", z3)
    z = z3 - z1 - z2
    print(" " * i * 4 + "z" + "'" * i + " = z3 - z1 - z2 = " + str(z3) + " - " + str(z1) + " - " + str(z2) + " = " + str(z))

    return (z1 * 10**(2*n2)) + ((z) * 10**n2) + z2


if __name__ == '__main__':
    # Test the function
    print("Multiplication P = 2052 * 1500", end="")
    num1 = 2052
    num2 = 1500
    result = karatsuba_multiplication(num1, num2 , 0)
    print("Result: P = z1*10^4 + z*10^2 + z2 =", result)