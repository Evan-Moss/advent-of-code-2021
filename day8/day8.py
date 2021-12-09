with open('input.txt', 'r') as file:
    f = file.readlines()
    input_list = [x.strip().split('|')[0].strip().split() for x in f]
    output_list = [x.strip().split('|')[1].strip().split() for x in f]

def unique(combo):
    if len(combo) == 2:
        return 1
    elif len(combo) == 3:
        return 7
    elif len(combo) == 4:
        return 4
    elif len(combo) == 7:
        return 8
    else:
        return False

num_unique = 0 
for o in output_list:
    for num in o:
        if unique(num):
            num_unique += 1

print(num_unique)