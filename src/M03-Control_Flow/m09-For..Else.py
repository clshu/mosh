successful = False

for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')

        break
else:  # This else block will only run if the for loop completes without a break
    print('Attempted 3 times and failed')
