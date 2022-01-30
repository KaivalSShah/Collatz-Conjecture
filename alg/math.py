number = int(input("starting positive integer: "))
run_till = int(input("Ending positive integer: "))
original_num = int(number)
i=0
iterations = {}
while i >= 0 and original_num <= run_till:
    def add_values_in_dict(sample_dict, key, list_of_values):
        sample_dict[key] = list()
        sample_dict[key].extend(list_of_values)
        return sample_dict
    if number == 1:
        iterations = add_values_in_dict(iterations, str(original_num), [str(i)])
        original_num += 1
        i = 0
        number = original_num
    if (number % 2) == 0:
        number = number / 2
        i+=1
    else:
        number = 3*number + 1
        i+=1
print(iterations)