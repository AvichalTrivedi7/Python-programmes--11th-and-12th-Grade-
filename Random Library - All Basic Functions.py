import random

# First Program
x = random.randint(1, 5)  # Random integer between 1 and 5
N = random.randrange(1, x + 1)  # Random number between 1 and x

print("First Program Output:")
for i in range(N):
    print(i, "#", random.uniform(i + 1, i + 5))  # Random float between i+1 and i+5

# Second Program
text = list("CBSEONLINE")  # Converting string to list for shuffling
random.shuffle(text)  # Shuffling the characters randomly
text = "".join(text)  # Converting list back to string

count = random.choice(range(3))  # Randomly picking 0, 1, or 2
c = random.choice([8, 9])  # Randomly choosing between 8 and 9

print("\nSecond Program Output:")
while text[c] != 'L':
    print(text[c] + text[count] + '*', end="")
    count += 1
    c -= 1

# Using random.choices() and random.sample()
numbers = list(range(1, 11))  # List of numbers from 1 to 10
random_choices = random.choices(numbers, k=5)  # Picks 5 random numbers (with replacement)
random_sample = random.sample(numbers, 5)  # Picks 5 random numbers (without replacement)

print("\n\nUsing random.choices (with replacement):", random_choices)
print("Using random.sample (without replacement):", random_sample)
