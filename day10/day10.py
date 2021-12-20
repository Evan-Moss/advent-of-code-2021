with open('input.txt', 'r') as file:
    input_list = [list(l.strip()) for l in file.readlines()]

opn = set(['<', '{', '(', '['])
cls = set(['>', '}', ')', ']'])

relations = { '{': '}', '[': ']', '(': ')', '<': '>', '}': '{' , ']': '[' , ')': '(', '>': '<' }

def evaluate(inp):
    if all(x in opn for x in inp):
        return inp
    for i in range(len(inp)):
        ch = inp[i]
        if ch in cls:
            if inp[i-1] != relations[ch]:
                #print('Expected {} but received {}'.format(relations[inp[i-1]], inp[i]))
                return inp[i]
            else:
                inp.pop(i)
                inp.pop(i-1)
                return evaluate(inp)

scores = {')': 3, ']': 57, '}': 1197, '>':25137}
errors = []
to_remove = []
for i in range(len(input_list)):
    inp = input_list[i]
    eval = evaluate(inp)
    if len(eval) == 1:
        errors.append(scores[eval])
        to_remove.append(i)

input_list = [input_list[r] for r in range(len(input_list)) if r not in to_remove]

print('Part 1: {}'.format(sum(errors)))

finish_scores = {')': 1, ']': 2, '}': 3, '>': 4}
scores = []

for inp in input_list:
    score = 0
    for i in reversed(inp):
        score = (score * 5) + finish_scores[relations[i]]
    scores.append(score)

scores = sorted(scores)
print('Part 2: {}'.format(scores[int(len(scores)/2)]))
