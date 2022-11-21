str1, str2 = input().split(',')
last_character_in_str2 = str2[-1]
count = 0
for i in str1:
    if i == last_character_in_str2:
        count += 1
print(count)