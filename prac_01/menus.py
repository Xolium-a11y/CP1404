name = input("Name: ")
print("(H)ello \n(G)oodbye \n(Q)uit")
choice = input("Enter your choice: ") .upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}.")
    elif choice == "G":
        print(f"Goodbye {name}.")
    else:
        print("Invalid choice.")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    choice = input("Enter your choice: ") .upper()

print("Thank you for shopping with us!")
