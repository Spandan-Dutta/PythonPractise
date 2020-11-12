# Given a three-digit number. FInd the sum of its digit.
num = int(input("Enter a three digit number: "))
a = num // 100 % 10
b = num // 10 % 10
c = num % 10
sum = a+b+c
print(sum)