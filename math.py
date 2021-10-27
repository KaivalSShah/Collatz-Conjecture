number = int(input("any real whole number: "))
i=0
while i >= 0:
    if number == 1:
        print("The number you inputted took " + str(i) + " iterations including 1.")
        break
    if (number % 2) == 0:
        number = number / 2
        print(number)
        i+=1
    else:
        number = 3*number + 1
        print(number)
        i+=1