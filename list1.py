#print sum of first 10 even numbers
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

cnt = 0
sum = 0

for i in list:
    if i % 2 == 0:
        sum = sum + i
        cnt = cnt + 1

        if cnt == 10:
            break

print("sum is:", sum)



#accept two values S and N.print square of first N numbers starting from S

S = int(input("Enter S: "))
N = int(input("Enter N: "))

for i in range(S, S + N):
    print(i * i)

#reverse the accepted string

string = input("Enter a string: ")

print(string[::-1])

#accept sentence from user and cnt the vowels

sentence = input("Enter a sentence: ")

cnt = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')

print("Number of vowels:", cnt)

#remove duplicates from 

numbers = [1,2,3,2,4,1,5,3]

numbers = list(set(numbers))

print(numbers)

#reverse the list

numbers = [10,20,30,40,50]

print(numbers[::-1])
