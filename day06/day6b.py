with open('input.txt', 'r') as file:
    input_list = [int(f) for f in file.readline().strip().split(',')]

fish_counts = {
    0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0
}

for fish in input_list:
    fish_counts[fish] += 1

for day in range(1,257):
    new_fish = fish_counts[0]

    for x in range(len(fish_counts)-1):
        fish_counts[x] = fish_counts[x+1]
    
    fish_counts[6] += new_fish
    fish_counts[8] = new_fish

print(sum(fish_counts.values()))