# Quiz 1 - Print even numbers from 1 to 9 and count them
count = 0

for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"Total even numbers: {count}")
