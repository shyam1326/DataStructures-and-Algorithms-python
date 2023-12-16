


def bubble_sort(elements):

    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                elements[j+1], elements[j] = elements[j], elements[j+1]
                swapped = True
        
        if not swapped:
            break
        
    return elements



if __name__=="__main__":
    # num = [7,1,4,6]
    num = [1,4,6]
    print(bubble_sort(num))


