'''
Algorithm:

1. Initialize a for loop between the lower and upper ranges
2. Use the primeCheck function to check if the number is a prime or not
3. If not prime, break the loop to the next outer loop
4. If prime, print it.
5. Run the for loop till the upperRange is reached.

'''

lower_range = int(input("Enter Lower Range: "))
upper_range = int(input("Enter Upper Range: "))
print("Prime numbers between", lower_range, "and", upper_range, "are:")
for num in range(lower_range, upper_range + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)