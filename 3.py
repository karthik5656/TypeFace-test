possible_numbers = ['1', '2', '5', '6', '8', '9', '0']

n = int(input())
count = 0
i = 1
while True:
    x_str = set(str(i))
    p = True
    for digit in x_str:
        if digit not in possible_numbers:
            p = False
            break
    if p:
        count += 1
    if count == n:
        print(i)
        break
    i += 1