my_string = input()
int_list = [int(letter) for letter in my_string]
counter = 0
average_list = []
while counter < len(my_string) - 1:
    average_list.append((int_list[counter] + int_list[counter + 1]) / 2)
    counter += 1
print(average_list)
