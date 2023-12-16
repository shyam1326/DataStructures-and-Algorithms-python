
def binary_search(num_list, val_to_find):

    left_index = 0
    right_index = len(num_list) - 1

    while left_index <= right_index:

        middle_index = (left_index + right_index) //2

        middle_number = num_list[middle_index]

        if middle_number == val_to_find:
            print(f"Th value {val_to_find} is found in the list at {middle_index} index")
            return middle_index
        
        elif middle_number < val_to_find :
            left_index = middle_index + 1
        
        else:
            right_index = middle_index - 1

    print(f"The value {val_to_find} not found in list")

    return -1 

def find_occurance(num_list, val_to_find):
    result = []
    index = binary_search(num_list, val_to_find)

    # Left occurence
    left = index

    while left>=0:
        if num_list[left] == val_to_find:
            result.append(left)
        left = left - 1

    right = index+1

    while right< len(num_list):
        if num_list[right] == val_to_find:
            result.append(right)

        right = right + 1 
    
    return sorted(result)



if __name__=="__main__":

#1.When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?
# numbers = [1,4,6,9,10,5,7].
# Because the list is not sorted.

#2. Find index of all the occurances of a number from sorted list

    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15 
    print(find_occurance(numbers, number_to_find))
