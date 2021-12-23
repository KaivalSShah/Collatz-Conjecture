### In Progress. Fails, for now.

range_val = int(input("range_val max for iterations: "))
store_iterations = {}
iterations_val = 0
for number in range(range_val):
    while number >= 1:
        if number == 1:
            iterations_val +=1
            print(number, " --> ", iterations_val)
        if (number % 2) == 0:
            number = number / 2
            # print(number)
            iterations_val +=1
        else:
            number = 3*number + 1
            # print(number)
            iterations_val +=1