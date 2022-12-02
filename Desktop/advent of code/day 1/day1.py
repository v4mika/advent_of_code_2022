input = open("input.txt")

elf = 1
calorieSum = 0
maxSum = ()

for line in input:
    if line.strip():
        calorieSum += int(line)
    else:
        elf += 1
        if (not maxSum or calorieSum > maxSum[1]):
            maxSum = (elf, calorieSum)
        calorieSum = 0

print(maxSum)
    
