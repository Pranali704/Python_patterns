count=0
num=int(input("Enter no:"))

while num>0:
    count += 1
    num=num // 10
print(count)