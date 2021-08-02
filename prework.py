#Print a greating for a user

def hello_name(user_name):
    """Display a simple greeting."""
    name = user_name.upper()
    print("Hello, " + name + "!")

#hello_name('owen')

#Print odd numbers less than 100
current_number = 0
#while current_number < 100:
    current_number += 1
    if current_number % 2 == 0:
        continue
        
    #print(current_number)

#Print max number in list
def max_num_in_list(a_list):
    max = a_list[0]
    
    for x in a_list:
        if x > max:
            max = x
    
    return max

a_list = [1, 9, 2, 11, 15, 7, 29, 6]

#print(max_num_in_list(a_list))


#Print True or False for if the year entered is a leap year

#def is_leap_year(a_year):
    """Determines if a year is a leap year."""
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
    
    return leap

#is_leap_year(1996)


#Determine if a list contains consecutive items

#def is_consecutive(a_list):
    """Determine if numbers in a list are consecutive."""
    #Sort the list into ascending numberical value.
    a_list = sorted(a_list)
    #Review the value based on its index after being sorted.
    for index in range(len(a_list)):
        if a_list[index] == a_list[-1]:
            x = 'True'
        elif a_list[index] + 1 == a_list[index + 1]:
            continue
        else:
            x = 'False'
            break
    return x

list = [1,2,5,3,4]

#print(is_consecutive(list))



list2 = [1,5,9,6,7,8,2]
#print(is_consecutive(list2))