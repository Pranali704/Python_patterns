#create a list of 10 numbers and displaye the sum of last 4 elements

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Sum of last 4 elements:", sum(numbers[:-4]))

#remove the items from the list located at second and fifth position

numbers.pop(4)
numbers.pop(1)

print(numbers)

#print the diff bet highest and lowest of the list

print("Difference:", max(numbers) - min(numbers))

#append a num element in a list which is half of the item of third position 
numbers.append(numbers[2] // 2)
print(numbers)


