import math
def main():
    a, b, c, = eval(input("please enter the coefficients (a, b, c ): "))
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("the solutions are:", root1, root2 )


main()
