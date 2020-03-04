#Mirror the words in any given string

def enter_sent():
    pass
    sentence = input("Enter any sentence and I will mirror it: ")
    reverse = list(sentence)
    list.reverse(reverse)
    result = " ".join(reverse)
    print(result)

enter_sent()

ans = input("Try again?: ")
if ans == "Y":
    try_again = True
else:
    try_again = False


while try_again == True:
    enter_sent()
    ans = input("Try again?: ")
    if ans == "Y":
        try_again = True
    else:
        try_again = False

print("Thanks! Have a nice day!")

