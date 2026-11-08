
n = int(input())
a = list(map(int, input().split()))

freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

ans = 0

for i in freq:
    c = freq[i]

    if c >= i:
        ans += c - i
    else:
        ans += c

print(ans)
