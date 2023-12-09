
# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take 
# from a user using input() function

max_num = int(input("Enter a number: "))
odd_numbers = []
[odd_numbers.append(i) for i in range(1, max_num + 1) if i % 2 != 0]
print(f"The list of odd number for {max_num} is {odd_numbers}")