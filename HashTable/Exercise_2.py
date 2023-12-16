
# 3.poem.txt Contains famous poem "Road not taken" by poet Robert Frost. You have to read this file in python and print every word 
# and its count as show below. Think about the best data structure that you can use to solve this problem and figure out why you 
# selected that specific data structure.


poem_dict = {}
with open('dataset/poem.txt') as file:
    for line in file:
        tokens = line.split(' ')
        for each_word in tokens:
            each_word = each_word.replace('\n', '')
            if each_word in poem_dict:
                poem_dict[each_word] +=1
            else:
                poem_dict[each_word] = 1

print(poem_dict)
print(sorted(poem_dict.items(), key = lambda x:x[1], reverse=True))

















