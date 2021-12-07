# This is a bad solution
with open('input.txt', 'r') as file:
    input_list = [int(f) for f in file.readline().strip().split(',')]

fish_list = []

class Lanternfish:
    def __init__(self, days):
        self.days = days
    
    def __str__(self):
        return str(self.days)
    
    def __repr__(self):
        return self.__str__()
    
    def day_passed(self):
        if self.days > 0:
            self.days -= 1
        else:
            self.days = 6
            fish_list.append(Lanternfish(9))

for i in input_list:
    fish_list.append(Lanternfish(i))

print(len(fish_list))

for x in range(1,81):
    for fish in fish_list:
        fish.day_passed()

answer = len(fish_list)