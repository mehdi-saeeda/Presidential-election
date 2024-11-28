def main(n):
    winner = 0

    for i in range(2, n + 1):
        winner = (winner + 2) % i
    return winner + 1
n = int(input("enter the number : "))
print(main(n))
