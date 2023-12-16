

def recursive_search(num_list, val_to_find, left_index, right_index):

    # if left_index < 0 or right_index > len(num_list):
    #     return  
    
    if right_index < left_index :
        print(f"The value {val_to_find} not found in list")
        return -1
    
    middle_index = (left_index + right_index) //2
    middle_number = num_list[middle_index]

    if middle_number == val_to_find:
        print(f"Th value {val_to_find} is found in the list at {middle_index} index")
        return middle_index
    
    elif middle_number < val_to_find :
        left_index = middle_index + 1
    
    else:
        right_index = middle_index - 1
    
    return recursive_search(num_list, val_to_find, left_index, right_index)


if __name__=="__main__":
    num = [1,4,6,8,9,12,20,34]
    val = 50
    recursive_search(num, val, 0, len(num)-1)