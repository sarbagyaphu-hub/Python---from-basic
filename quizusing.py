# Welcome
def welcome():
    print("Welcome to the quiz game created using Python")


# Player details
def player_details():
    var_name = input("Please enter your name:\n")
    return var_name


# Select mode
def modes():
    print("Please choose one mode")
    var_mode = input(
        "Type e for easy, m for medium, or h for hard:\n"
    ).lower()

    return var_mode


# Quiz game
def game(var_mode):
    if var_mode == "e":
        print(
            "\nWhat is the total area of Nepal?"
            "\na) 147,181 sq km"
            "\nb) 147,182 sq km"
            "\nc) 123,456 sq km"
            "\nd) 147,516 sq km"
        )

        var_q1 = input("The correct option is:\n").lower()

        if var_q1 == "a":
            print("Your answer is correct")
        else:
            print("Wrong answer")

    elif var_mode == "m":
        print(
            "\nWhat is the biggest district of Nepal?"
            "\na) Dolpa"
            "\nb) Kathmandu"
            "\nc) Bhaktapur"
            "\nd) Lalitpur"
        )

        var_q2 = input("The correct option is:\n").lower()

        if var_q2 == "a":
            print("Your answer is correct")
        else:
            print("Wrong answer")

    elif var_mode == "h":
        print(
            "\nWhat is Albert Einstein's famous formula?"
            "\na) E = mc²"
            "\nb) c = me²"
            "\nc) m = ec²"
            "\nd) E = mc³"
        )

        var_q3 = input("The correct option is:\n").lower()

        if var_q3 == "a":
            print("Your answer is correct")
        else:
            print("Wrong answer")

    else:
        print("Invalid mode. Please enter e, m, or h.")


# Complete
def complete():
    print("You played well. See you soon!")


# Run the program
welcome()

player_name = player_details()
print("Hello,", player_name)

selected_mode = modes()
game(selected_mode)

complete()
