import os, sys
with open(os.path.join(sys.path[0],'input.txt'), 'r') as file:
    f = file.readlines()
    input_list = [[set(y) for y in x.strip().split('|')[0].strip().split()] for x in f]
    output_list = [[set(y) for y in x.strip().split('|')[1].strip().split()] for x in f]

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

def find_unique(inp):
    remove = []
    for num in inp:
        if unique(num):
            solved_numbers[unique(num)] = num
            remove.append(num)
    [inp.remove(r) for r in remove]
    return inp

def find_combo_nums(inp):
    remove = []
    for num in inp:
        if len(num) == 5 and solved_numbers[7].issubset(num):
            solved_numbers[3] = num 
            remove.append(num)
        if len(num) == 6 and solved_numbers[4].issubset(num):
            solved_numbers[9] = num 
            remove.append(num)
    [inp.remove(r) for r in remove]
    return inp

def find_final_nums(inp):
    for num in inp:
        if len(num) == 5 and num.issubset(solved_numbers[9]):
            solved_numbers[5] = num
        elif len(num) == 5:
            solved_numbers[2] = num
        elif len(num) == 6 and solved_numbers[1].issubset(num):
            solved_numbers[0] = num
        elif len(num) == 6:
            solved_numbers[6] = num

def get_output(out_line):
    out = ''
    for o in out_line:
        for k,s in solved_numbers.items():
            if o == (s):
                out += str(k)
    return int(out)

def solve_line(inp_line, out_line):
    inp = find_unique(inp_line)
    inp = find_combo_nums(inp)
    find_final_nums(inp)
    return get_output(out_line)
    
outs = []
for i in range(len(input_list)):
    solved_numbers = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{}}
    out = solve_line(input_list[i], output_list[i])
    outs.append(out)

print('Answer: {}'.format(sum(outs)))