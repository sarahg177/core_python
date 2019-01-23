def even_number_of_evens(numbers):
    #check to see if array is empty
    if numbers == []:
        return False
    else:
       #set evens variable to 0
       evens = 0
    
    # check to see if number is divided by 2 then the remainder is 0 
    for number in numbers:
        if number %2 == 0:
            # increment evens variable by 1
            evens +=1
    
    # if 0 is divided by 2 the answer will be 0 so add if evens == 0 return false
    if evens == 0:
        return False
    #check to see if the number of evens when divided by 2 then the remainder is 0        
    return evens %2 == 0
       
         
         

assert even_number_of_evens([]) == False, "No numbers"   
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")