print("start the numeric guess game")
j=18
noguess = 1
print("number of guess limited 7 times")
while (noguess<=9):
    no=(int(input("guess the number\n")))
    if (no<j):
     print("you enter less number please,enter greater number.\n")
    elif (no>j):
     print("you enter greater number please,enter smaller number.\n ")
    else:
        print("you enter a correct number","congragulations you won")
        print(noguess,"no.of guesses you took to finish.")
        break
    print(9-noguess,"no. of guesses you left")
    noguess=noguess+1

if(noguess>9):
    print("gamer over buddy")




















#