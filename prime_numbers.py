minimum_number = int(input("Enter Minimum Number: "))
maximum_number = int(input("Enter Maximum Number: "))
for number in range(minimum_number, (maximum_number + 1)):
    print(number)


prime_number = []
for number in range(1, 100):
    if number > 1:
        for value in range(2, number):
            if(number % value) == 0:
                break
        else:
            prime_number.append(number)
print(prime_number)
print(sum(prime_number))
average = sum(prime_number) / len(prime_number)
print(average)
