

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



if __name__=="__main__":
    num = [1,4,6,8,9,12,20,34]
    val = 5
    binary_search(num, val)