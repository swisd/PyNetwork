def main():
    n = eval(input("please enter a whole number:  "))
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("the factorial of", n, "is", fact)


main()
