
import random

frequency = [0, 0, 0, 0, 0, 0]

rolls = int(input("Enter number of rolls: "))

for i in range(rolls):
    result = random.randint(1, 6)
    print("Roll", i + 1, ":", result)
    frequency[result - 1] += 1

print("\nDice Frequency:")

for i in range(6):
    print(i + 1, "appeared", frequency[i], "times")
