######################################################################
###                       DICE ROLLING GAME                        ###
######################################################################

import random


def main():
    while True:
        choice = input("Roll the dice? (y/n): ").lower()
        if choice == "y":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"({die1}, {die2})")
        elif choice == "n":
            print("Thank you")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
