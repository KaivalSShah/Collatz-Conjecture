import pandas as pd

number = int(input("starting positive integer: "))
run_till = int(input("Ending positive integer: "))
run_for = run_till - number
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
x_axis = []
y_axis = []

for value_y in list(iterations.values()):
    individual_value_y = value_y[0]
    y_axis.append(individual_value_y)

for value_x in list(iterations.keys()):
    x_axis.append(value_x)

for i in range(0, len(x_axis)):
    x_axis[i] = int(x_axis[i])
    y_axis[i] = int(y_axis[i])

print(x_axis)
print(y_axis)
df = pd.DataFrame({'number': x_axis, 'iterations': y_axis})
df.to_excel('./../data/collatz.xlsx')