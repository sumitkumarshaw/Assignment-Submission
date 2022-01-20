'''
Day 3 Assignment
taking user input and storing the user input in a list
and printing the details in fstring
'''

total_input=list()
total_input.append(input("Enter Your Name::"))
total_input.append(int(input("Enter Your Age::")))
total_input.append(input("Enter Your Gender::"))
total_input.append(input("Enter Your Address::"))
total_input.append(input("Enter Your Highest Qualification::"))
total_input.append(float(input("Enter Your Salary::")))
total_input.append(input("Enter Your Fathers Name::"))
total_input.append(input("Enter Your Mothers Name::"))

print(f'Personal Details')
print(f'Name={total_input[0]}')
print(f'Age={total_input[1]}')
print(f'Gender={total_input[2]}')
print(f'Address={total_input[3]}')
print(f'Highest Qualification={total_input[4]}')
print(f'Salary={total_input[5]}')
print(f'Fathers Name={total_input[6]}')
print(f'Mothers Name={total_input[7]}')

