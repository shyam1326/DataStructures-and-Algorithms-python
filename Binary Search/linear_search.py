

def linear_search(num_list, val_to_find):
    for index,ele in enumerate(num_list):
        if ele == val_to_find:
            print(f"Th value {val_to_find} is found in the list at {index} index")
            return index
        else:
            continue
    print(f"The value {val_to_find} not found in list")
    return -1




if __name__=="__main__":
    num = [1,4,6,8,9,12,20,34]
    val = 5
    linear_search(num,val)
