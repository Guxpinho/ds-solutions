# Loop through numbers from 5 to 100
for numero in range(5, 101):
    # Check if divisible by 7 and NOT divisible by 5
    if numero % 7 == 0 and numero % 5 != 0:
        # Print numbers on the same line separated by spaces
        print(numero, end=' ')
