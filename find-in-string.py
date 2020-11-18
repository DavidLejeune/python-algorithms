# Given a string , find the first uppercqse character
# Solve using both iterative and recursive solution

input_str_1 = "elvisPresley"
input_str_2 = "ElvisPresley"
input_str_3 = "elvispresley"

print("Given a string , find the first uppercqse character")
print("Solved using both iterative and recursive solution")
print('---------------------------------------------------\n')

print("String 1: " + input_str_1)
print("String 2: " + input_str_2)
print("String 3: " + input_str_3 + "\n")



def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return "String : " + input_str + " > Position : " + str(i) +  " | Character : " + input_str[i]
    return "String : " + input_str + " > No uppercase character found"

print("Iterative method :")
print("------------------")

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print('')

def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx].isupper():
        return "String : " + input_str + " > Position : " + str(idx) +  " | Character : " + input_str[idx]
    if idx == len(input_str) - 1:
        return "String : " + input_str + " > No uppercase character found"
    return find_uppercase_recursive(input_str, idx+1)

print("Recursive method :")
print("------------------")

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))