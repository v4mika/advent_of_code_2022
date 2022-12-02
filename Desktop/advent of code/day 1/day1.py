input = open("input.txt")

elf = 1
calorieSum = 0
maxThree = [0]
minOfThree = 0

for line in input:
    if line.strip():
        calorieSum += int(line)
    else:
        elf += 1
        
        if calorieSum > minOfThree:
            maxThree.remove(minOfThree)
        
        if len(maxThree) < 3:
            maxThree.append(calorieSum)
            minOfThree = min(maxThree)

        
        calorieSum = 0

print(sum(maxThree))
    
