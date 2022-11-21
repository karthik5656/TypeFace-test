n = int(input())
ans = ''
while n:
    ans += str(n % 3)
    n = n // 3
ans = ans[::-1]
print(ans)