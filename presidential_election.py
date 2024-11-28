def main(n):
    winner = 0
    for i in range(2, n + 1):
        winner = (winner + 2) % i
    return winner + 1

def get_input():
    while True:
        try:

            n = input("Enter the number (2 ≤ n ≤ 100). ")
            if not n.isdigit():
                print("Invalid input Please enter a valid integer.")
                continue
            n = int(n)

            if n < 2 or n > 100:
                print("The number must be between 2 and 100.")
                continue
            return n

        except ValueError:
            print("Invalid input Please enter a valid integer.")

n = get_input()

print(f"The winner is: {main(n)}")
