# Main function to calculate the winning candidate number
def main(n):
    winner = 0    # Initialize winner index to 0 (starting point)
    for i in range(2, n + 1):
        winner = (winner + 2) % i
    return winner + 1

# Function to get valid input from the user
def get_input():
    while True:     # Repeat until valid input is received
        try:

            n = input("Enter the number (2 ≤ n ≤ 100). ")
            if not n.isdigit():
                print("Invalid input Please enter a valid integer.")
                continue
            n = int(n)

            if n < 2 or n > 100:
                print("The number must be between 2 and 100.")
                continue
            return n  # Return the valid input

        except ValueError:
            print("Invalid input Please enter a valid integer.")

# Get the number from the user
n = get_input()

print(f"The winner is: {main(n)}")
